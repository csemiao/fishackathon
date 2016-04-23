#
# This script populates the database with for stream temps
#

import os
import sys


script_path = os.path.dirname(__file__)
project_dir = os.path.abspath(os.path.join(script_path, '../','..','fishackathon2016'))
sys.path.insert(0, project_dir)

# Set the django settings module to the symlink in the scripts directory (which points to the actual file)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

import xml.etree.ElementTree as eTree
import datetime

from carp_watcher.models import Stream, Data_Stream_Temp

def setup_test_stream_data():
    """
    Parses an XML file containing stream information and daily temperature information for that stream
    -Stream
        - Name
    -Data
        -Date {month, day, year}
            - Temp
    """

    stream_tree = eTree.parse('test_data.xml').getroot()
    stream_name = stream_tree.find('stream').text

    stream_ins = create_stream(stream_name)
    data = stream_tree.find('data')
    create_data(data, stream_ins)


def create_stream(stream_name):
    """
    Populates the database with a stream object
    :param stream_name: {String} Stream name
    :return: {Model.objects.Stream}  Instance of stream model corresponding to inputted name
    """
    stream_ins = Stream.objects.get_or_create(name=stream_name)[0]
    return stream_ins

def create_data(data, stream_ins):
    """
    Populates the database with temperature data for a stream
    :param data: {Element.list} A list of eTree objects with date and temperature information
    :param stream_ins: Stream model instance to which the data belongs
    :return: void
    """

    for date in data:
        year = int(date.attrib['year'])
        month = int(date.attrib['month'])
        day = int(date.attrib['day'])

        date_obj = datetime.date(year, month, day)
        temp = date.find('temp').text
        stream_data_obj = Data_Stream_Temp.objects.get_or_create(stream=stream_ins, day=date_obj, temp=temp)
        print('added day: ' + str(date_obj) + ' temp ' + temp)

setup_test_stream_data()


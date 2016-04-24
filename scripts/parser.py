import os
import sys

script_path = os.path.dirname(__file__)
project_dir = os.path.abspath(os.path.join(script_path, '../','..','fishackathon2016'))
sys.path.insert(0, project_dir)

# Set the django settings module to the symlink in the scripts directory (which points to the actual file)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

from lxml import html
import requests
from carp_watcher.models import Stream, Data_Stream
from datetime import datetime
from dateutil.parser import parse
from itertools import *
from decimal import Decimal
import re
import sys;
reload(sys);
sys.setdefaultencoding("utf8")


page = requests.get('http://waterdata.usgs.gov/mi/nwis/uv?cb_00055=on&cb_00010=on&format=html&site_no=04119400&period=&begin_date=2016-01-01&end_date=2016-04-01')
tree = html.fromstring(page.content)

stream = tree.xpath('/html/body/h2/text()')
stream = stream[0]

date = tree.xpath('/html/body/table[1]/tbody//tr/td[1]/text()')
# print "Dates Jan - April", date

velocity = tree.xpath('/html/body/table[1]/tbody/tr/td[2]/text()')
# print "Velocity Jan - April", velocity

temp = tree.xpath('/html/body/table[1]/tbody/tr/td[3]/text()')
# print "Temperature Jan - April", temp


def format_date(date):
    stripped_date = [dateStr.strip('EST') for dateStr in date]
    stripped_date = [dateStr.rstrip() for dateStr in stripped_date]
    stripped_date = [parse(dateStr) for dateStr in stripped_date]
    return stripped_date


def format_temp(temp):
    stripped_temp = [re.sub('[^\d.]-', "", t) for t in temp]
    stripped_temp = [t.replace("\xc2\xa0", u'') for t in stripped_temp]
    stripped_temp = [t.encode('utf-8').strip() for t in stripped_temp]
    stripped_temp = [t.strip() for t in stripped_temp]
    # print stripped_temp
    stripped_temp = [str(t) for t in stripped_temp]
    f_temp = [re.sub('((?<=,)|^)(?=,|$)', '0.0', s) for s in stripped_temp]
    f_temp = [(Decimal(t) if t else 0.0) for t in f_temp]
    print f_temp
    return f_temp

def create_stream(stream_name):
    """
    Populates the database with a stream object
    :param stream_name: {String} Stream name
    :return: {Model.objects.Stream}  Instance of stream model corresponding to inputted name
    """
    stream_ins = Stream.objects.get_or_create(name=stream_name)[0]
    return stream_ins

create_stream("Atlantic ocean")
def create_data(stream, date, velocity, temp):
    """
    Populates the database with temperature data for a stream
    :param data: {Element.list} A list of eTree objects with date and temperature information
    :param stream_ins: Stream model instance to which the data belongs
    :return: void
    """
    date = format_date(date)
    stream = create_stream(stream)
    velocity = format_temp(velocity)
    temp = format_temp(temp)
    for d, v, t in izip(date, velocity, temp):
        date_obj = d
        vel = v
        temp = t
        stream_data_obj = Data_Stream.objects.get_or_create(stream=stream, day=date_obj, velocity=vel, temp=t)

create_data("holly", date, velocity, temp)

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
import numpy
reload(sys);
sys.setdefaultencoding("utf8")



def coffee_parse(begin, end):

    begin = begin
    end = end
    page = requests.get('http://waterdata.usgs.gov/mi/nwis/uv?cb_00055=on&cb_00010=on&format=html&site_no=04119400&period=&begin_date=' + begin + '&end_date=' + end)
    tree = html.fromstring(page.content)
    return tree


def s_stream(tree):
    stream = tree.xpath('/html/body/h2/text()')
    stream = stream[0]
    return stream


def v_velocity(tree):
    velocity = tree.xpath('/html/body/table[1]/tbody/tr/td[2]/text()')
    return velocity


def t_temp(tree):
    temp = tree.xpath('/html/body/table[1]/tbody/tr/td[3]/text()')
    return temp

def d_date(tree):
    date = tree.xpath('/html/body/table[1]/tbody//tr/td[1]/text()')
    return date


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
    stripped_temp = [str(t) for t in stripped_temp]
    f_temp = [re.sub('((?<=,)|^)(?=,|$)', '0.0', s) for s in stripped_temp]
    f_temp = [(Decimal(t) if t else 0.0) for t in f_temp]
    return f_temp

def create_stream(stream_name):
    """
    Populates the database with a stream object
    :param stream_name: {String} Stream name
    :return: {Model.objects.Stream}  Instance of stream model corresponding to inputted name
    """
    stream_ins = Stream.objects.get_or_create(name=stream_name, lat=0, long=0, length=0)[0]
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
    master = {}
    std = 0.7

    key = [datetime.date(d) for d in date]
    for k in key:
        if k not in master:
            master[key.index(k)] = k
    print master
    master_tup = master.items()
    print master_tup
    obv = 120
    l = len(master_tup)
    n = 0
    prev = 0
    sucks = 1
    if l == 1:
        next = len(date)
    else:
        next = master_tup[sucks][0]
    n_val = []
    for m in master_tup:
        n_val.append(m[0])
    n_val.append(len(date) - 1)
    n_val.sort()
    print n_val

    for k in range(n,l):

        print prev, next
        next = n_val[sucks]
        bd = date[prev:next]
        bv = velocity[prev:next]
        bt = temp[prev:next]
        jarjar = pleasework(bd, bv, bt)
        v = jarjar[0]
        t = jarjar[1]
        spike = True if Decimal(v) > 0.7 else False
        dd = master.get(prev)

        stream_data_obj = Data_Stream.objects.get_or_create(stream=stream, day=dd, velocity=v, temp=t,
                                                            spike=spike)

        prev = next
        print prev
        n = n + 1
        sucks = sucks + 1
        print next




def pleasework(date, velocity, temp):
    t_hash = {}
    v_hash = {}
    for d,v,t in zip(date, velocity, temp):
        date_obj = d
        mkey = d
        vel = v * Decimal(0.3048)
        temp = t
        value = [temp]
        v_val = [vel]
        if mkey in t_hash:
            t_hash[mkey].append(value)
        else:
            t_hash[mkey] = value

        if mkey in v_hash:
            v_hash[mkey].append(v_val)
        else:
            v_hash[mkey] = v_val

    effing_temp = t_hash.values()
    effing_vel = v_hash.values()
    print effing_vel
    print effing_temp
    print "cauli",  [sum(t) for t in zip(*effing_vel)][0]

    etemp_sum = [sum(t) for t in zip(*effing_temp)][0]
    avt = format(etemp_sum / len(effing_temp), '.2f')
    evel_sum = [sum(t) for t in zip(*effing_vel)][0]
    avl = format(evel_sum / len(effing_vel), '.2f')

    return [avl, avt]


def commence(begin, end):
    tree = coffee_parse(begin, end)
    stream = s_stream(tree)
    velocity = v_velocity(tree)
    temp = t_temp(tree)
    date = d_date(tree)
    create_data(stream, date, velocity, temp)

begin = '2016-01-01'
end = '2016-04-23'
commence(begin, end)


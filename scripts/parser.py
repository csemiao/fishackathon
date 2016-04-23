from lxml import html
import requests
from populate_test_data import populate_test_data


page = requests.get('http://waterdata.usgs.gov/mi/nwis/uv?cb_00055=on&cb_00010=on&format=html&site_no=04119400&period=&begin_date=2016-01-01&end_date=2016-04-23')
tree = html.fromstring(page.content)

stream = tree.xpath('/html/body/h2/text()')
print stream

date = tree.xpath('/html/body/table[1]/tbody//tr/td[1]/text()')
print "Dates Jan - April", date

velocity = tree.xpath('/html/body/table[1]/tbody/tr/td[2]/text()')
print "Velocity Jan - April", velocity

temp = tree.xpath('/html/body/table[1]/tbody/tr/td[3]/text()')
print "Temperature Jan - April", temp

def stream_create(stream_name):
    populate_test_data.create_stream(stream_name)

stream_create("hello")
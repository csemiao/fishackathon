from lxml import html
import requests

page = requests.get('http://waterdata.usgs.gov/mi/nwis/uv?cb_00055=on&cb_00010=on&format=html&site_no=04119400&period=&begin_date=2016-01-01&end_date=2016-04-23')
tree = html.fromstring(page.content)



date = tree.xpath('/html/body/table[1]/tbody//tr/td[1]/text()')
print "Dates Jan - April", date

velocity = tree.xpath('/html/body/table[1]/tbody/tr/td[2]/text()')
print "Velocity Jan - April", velocity

temp = tree.xpath('/html/body/table[1]/tbody/tr/td[3]/text()')
print "Temperature Jan - April", temp
__author__ = 'Sharad'

import urllib2
import json
commonUrl = ''
req = urllib2.Request('http://stats.grok.se/json/en/201407/apple')
response = urllib2.urlopen(req)
the_page = response.read()
data_in_json1 = json.dumps(the_page, sort_keys=True, indent=4, separators=(',', ':'))
data_in_json2 = json.dumps(json.loads(the_page))
data_in_json3 = json.dumps(json.loads(the_page), sort_keys=True, indent=4, separators=(',', ':'))

with open('workfile.json', 'w') as file:
    json.dump(json.loads(the_page), file, indent=4, separators=(',', ':'))
print data_in_json3
print file



__author__ = 'Sharad'

import urllib2
import json

commonUrl = 'http://stats.grok.se/json/en/'
keys = ['apple_inc', 'macbook air', 'macbook pro', 'imac', 'ipad air', 'ipad mini 2', 'iphone 5s', 'iphone 5c']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
years = ['2013', '2014']

txtFile = open('wikipediaCounts.txt', 'w')
# october data
for month in months:
    for year in years:
        for key in keys:
            url = commonUrl+'/'+year+month+'/'+key
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            the_page = response.read()
            with open(year+month+key+'.json', 'w') as file:
                json.dump(json.loads(the_page), file, indent=4, separators=(',', ':'))
            txtFile.write()


#!/usr/bin/env python
__author__ = 'cloudera'
import sys
import warc
from textblob import TextBlob
import string
import urllib
import os

commonPath = 's3://aws-publicdatasets/'

for line in sys.stdin:
    #download file
    url = commonPath+line
    os.system('aws s3 cp '+url+'./file.warc.wet.gz')
    print 'wet file downloaded'

    #open the warc file
    f = warc.open('file.warc.wet.gz')
    txtFile = open('data/'+line[70:140]+'.txt', 'w')

    #read the warc file and write to text file
    for record in f:
        if record['Content-Type'] == 'text/plain':
            date = record['WARC-Date']
            htmlText = record.payload.read()
            text = htmlText.strip()
            text = text.translate(None, '[!@#$+:|/\#%^*()-_=~]\n')
            printableText = filter(lambda x: x in string.printable, text)
            blob = TextBlob(printableText)
            for sentence in blob.sentences:
                if len(sentence) <= 340:
                    txtFile.write(date[0:10])
                    txtFile.write('\t')
                    txtFile.write(str(sentence))
                    txtFile.write('\n')

    #delete the downloaded warc file
    os.remove('file.warc.wet.gz')
    print 'warc file deleted'
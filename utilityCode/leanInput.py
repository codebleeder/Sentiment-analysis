#!/usr/bin/env python
__author__ = 'cloudera'
import sys
import warc
from textblob import TextBlob
import string
import urllib
import os

txtFile = open('input/march2014leanInput.txt', 'w')
count = 0

for line in sys.stdin:
    if count % 500 == 0:
        txtFile.write(line)
    count += 1

print 'done!'
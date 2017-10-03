#!/usr/bin/env python
__author__ = 'cloudera'
import sys
import warc
from textblob import TextBlob
import string
import urllib
import os

txtFile = open('input/march2014Wet.txt', 'w')
count = 0

for line in sys.stdin:
    lineSplit = line.split(' ')
    print len(lineSplit)
    if len(line) == 169:
        if line[162:165] == 'wet':
            txtFile.write(lineSplit[-1])

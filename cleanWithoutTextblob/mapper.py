#!/usr/bin/env python
__author__ = 'cloudera'
import sys

for line in sys.stdin:
    (date, sentence) = (line[0:10], line[11:-1])
    sentenceSplit = sentence.split()
    for word in sentenceSplit:
        if (
            word == 'apple' or
            word == 'iphone' or
            word == 'ipad' or
            word == 'macintosh' or
            word == 'osx'
        ):
            print "%s\t%s" % (date, line[11:-1])

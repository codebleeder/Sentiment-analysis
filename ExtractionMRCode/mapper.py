#!/usr/bin/env python
__author__ = 'cloudera'

import sys
from textblob import TextBlob
import nltk

for line in sys.stdin:
    (date, sentence) = (line[0:10], line[11:-1])
    sentenceBlob = TextBlob(sentence)
    for nounPhrase in sentenceBlob.noun_phrases:
        if (
            nounPhrase == 'apple' or
            nounPhrase == 'iphone' or
            nounPhrase == 'ipad' or
            nounPhrase == 'mac' or
            nounPhrase == 'osx'
        ):
            print "%s\t%s" % (date, line[11:-1])



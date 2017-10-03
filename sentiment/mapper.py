__author__ = 'cloudera'

from textblob import TextBlob
import sys

for line in sys.stdin:
    (date, sentence) = (line[0:10], line[11:-1])

    sentenceBlob = TextBlob(sentence)
    sentiment = str(sentenceBlob.sentiment.polarity)+'\t'+str(sentenceBlob.sentiment.subjectivity)
    print "%s\t%s" % (line.strip(), sentiment)
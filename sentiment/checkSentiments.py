__author__ = 'cloudera'

from senticnet.senticnet import Senticnet
from textblob import TextBlob

sentence = "One of the very first Apple 1 computers, worth about 500,000, goes on sale later this month at Christie's auction house, the latest vintage tech sale."

sn = Senticnet()

concept_info = sn.concept('love')
print 'sn.concept(love) = ', concept_info

polarity = sn.polarity('love')
print 'polarity(love) = ', polarity

semantics = sn.semantics('love')
print 'semantics = ', semantics

sentics = sn.sentics('love')
print 'sentics = ', sentics

sentenceBlob = TextBlob(sentence)
print sentenceBlob.parse()
print sentenceBlob.sentiment

sentenceConcept = sn.concept(sentence)
print sentenceConcept
__author__ = 'cloudera'
import sys

txtFile = file('refinedPageViews.txt', 'w')
for line in sys.stdin:
    line2 = line.strip()
    print line2[13:-1]
    out = line2[1:11]+'\t'+line2[13:-1]+'\n'
    txtFile.write(out)
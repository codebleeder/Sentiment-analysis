__author__ = 'cloudera'

import sys

txtFile = file('refinedStats.txt', 'w')
count = 0

for line in sys.stdin:
    line2 = line.strip()
    if count % 2 == 0:
        txtFile.write(line)
        print line2
    count = count + 1
__author__ = 'cloudera'

import os
import sys

for line in sys.stdin:
    # line is file name.
    # append with path
    path = 'data/'+line.strip()
    print path
    os.system('cat'+' '+path+'|'+'python mapper.py > cleanData/'+line)
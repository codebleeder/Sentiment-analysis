__author__ = 'cloudera'

import os
import sys

for line in sys.stdin:
    # line is file name.
    # append with path
    path = '../cleanData2/'+line.strip()
    print path
    os.system('cat'+' '+path+'|'+'python mapper.py > ../totalData/'+line)
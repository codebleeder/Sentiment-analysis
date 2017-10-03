__author__ = 'cloudera'
import os
for filename in os.listdir("data/"):
    print filename[0:28]
    os.rename('data/'+filename, 'data/'+filename[0:28])
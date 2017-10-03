__author__ = 'cloudera'
from subprocess import call
import sys
import os

ec2 = 'ec2-user@ec2-54-165-49-104.compute-1.amazonaws.com'
pemPath = '/home/cloudera/Downloads/awsCredentials/sharadKeyPairNVirginia.pem'

#call['scp', '-i '+pemPath+' '+sys.argv[1]+' '+ec2]
os.system('scp '+'-i '+pemPath+' '+sys.argv[1]+' '+ec2)

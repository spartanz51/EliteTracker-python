#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
import sys
from elitetracker.elitetracker import *

any_result = False
err = False
first_download = False

for arg in sys.argv:
    if arg == "--first":
		first_download = True
		
x = Elite_Tracker()
try:
	result = x.search_torrent(sys.argv[1])
except:
	print "Usage: python2 elite-download.py <search>"
	sys.exit(0)

for i in range (0, len(result)):
	any_result = True
	if not first_download:
		print str(i+1)+". "+result[i][1]	
	
if any_result:
	if not first_download:		
		try:
			to_dl = input("Download > ")
		except:
			err = True
	else:
		to_dl = 1
else:
	print "No result"
	sys.exit(0)

if not err and str(to_dl).isdigit() and 0 < to_dl <= len(result):
	x.download_torrent(result[to_dl - 1][0])
else:
	print "Usage: id of torrent (ex: 1)"
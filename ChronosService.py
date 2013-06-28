#!/usr/bin/env python
import ChronosTool
import time
from pync import Notifier
import serial
import sys
import os
import datetime
import pprint
import copy

try:
	bm = ChronosTool.CBM( "/dev/cu.usbmodem001" )
except serial.serialutil.SerialException:
	print "Could not open device."
	sys.exit()
while 1:
	if bm.spl_status() != None:
		Notifier.notify('Found watch.', title='Chronos Watch')
		dldata = copy.copy(bm.spl_download())
		bm.spl_sync()
		pprint.pprint(dldata)
		if dldata != None:
			timestamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S.bin")
			file = open(timestamp,"wb")
			file.write(dldata)
			file.close()
			# subprocess.Popen("java in.tomj.DatalogFileReader",shell=true)
			Notifier.notify('Sync complete.', title='Chronos Watch')
			time.sleep(5) # This sleep is necessary to give the watch enough time to erase the flash.
			bm.spl_erase()
			time.sleep(5)
			pprint.pprint(dldata)
		else:
			Notifier.notify('Sync failed.', title='Chronos Watch')
		bm.spl_goodbye()
		# time.sleep(300) #Maybe put a keyboard exception here.
	time.sleep(5)



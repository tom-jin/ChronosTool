#!/usr/bin/env python
import ChronosTool
import time
from pync import Notifier
import serial
import sys
import os
import datetime

try:
	bm = ChronosTool.CBM( "/dev/cu.usbmodem001" )
except serial.serialutil.SerialException:
	print "Could not open device."
	sys.exit()
while 1:
	if bm.spl_status() != None:
		Notifier.notify('Found watch.', title='Chronos Watch')
		data = bm.spl_download()
		if data != None:
			timestamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S.bin")
			file = open(timestamp,"wb")
			file.write(data)
			file.close()
			Notifier.notify('Sync complete.', title='Chronos Watch')
			bm.spl_sync()
			bm.spl_erase()
			bm.spl_goodbye()
		else:
			Notifier.notify('Sync failed.', title='Chronos Watch')

		# time.sleep(300) #Maybe put a keyboard exception here.
	time.sleep(5)

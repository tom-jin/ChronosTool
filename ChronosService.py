#!/usr/bin/env python
import ChronosTool
import time
import serial
import sys
import os
import datetime
import pprint
import copy
import ParseMemory

try:
	device_guess = ["/dev/ttyUSB0", "/dev/cu.usbmodem001", "/dev/ttyACM0"]
	for path in device_guess:
		if os.path.exists( path ):
			device = path
	bm = ChronosTool.CBM( device )
except serial.serialutil.SerialException:
	print "Could not open device."
	sys.exit()
while 1:
	if bm.spl_status() != None:
		print "Found watch"
		dldata = copy.copy(bm.spl_download())
		bm.spl_sync()
		if dldata != None:
			timestamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S.bin")
			file = open(timestamp,"wb")
			file.write(dldata)
			file.close()
			print "Sync Complete. File written to ", timestamp
			time.sleep(5) # This sleep is necessary to give the watch enough time to erase the flash.
			bm.spl_erase()
			ParseMemory.parseWatchMemory(timestamp, timestamp + ".csv")
			time.sleep(5)
		else:
			print "Sync failed."
		bm.spl_goodbye()
		# time.sleep(300) #Maybe put a keyboard exception here.
	time.sleep(1)



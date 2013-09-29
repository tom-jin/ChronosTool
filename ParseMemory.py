#!/usr/bin/python
import sys
from sys import argv
import struct
from pprint import pprint
import datetime
import csv

def parseHeader(header):
	sessionbegin, null, day, month, year, hour, minute, second = struct.unpack('HHBBHBBB', header)
	if sessionbegin != 0xFFFB:
		print "Error: Invalid file."
	starttime = datetime.datetime(year, month, day, hour, minute, second)
	print "Message: Found session begin marker. " + str(starttime)
	return starttime

def parseWatchMemory(inputfilename, outputfilename):
	inputfile = open(inputfilename, "rb")
	outputfile = open(outputfilename, "w")
	outputwriter = csv.writer(outputfile)

	time = parseHeader(inputfile.read(11))
	timedelta = datetime.timedelta(0,0,50000)

	reading = inputfile.read(3)
	while len(reading) == 3:
		x, y, z = struct.unpack('bbb', reading)
		if  x == -2 and y == -1 and z == -5:
			print "Message: Found session end marker."
			nextheader = inputfile.read(10)
			if len(nextheader) < 10:
				sys.exit(0)
			time = parseHeader("\xFB" + nextheader)
			reading = inputfile.read(3)
			x, y, z = struct.unpack('bbb', reading)
		outputwriter.writerow([time,18*x,18*y,18*z])
		time += timedelta
		reading = inputfile.read(3)	

if __name__ == "__main__":
	if len(argv) < 2:
		print "Missing filename."
		sys.exit(0)
	if len(argv) == 2:
		script, inputfilename = argv
		outputfilename = "a.out"
	else:
		script, inputfilename, outputfilename = argv[:3]
	parseWatchMemory(inputfilename, outputfilename)

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
	timedelta = datetime.timedelta(0,10)

	reading = inputfile.read(1)
	while len(reading) == 1:
		x = struct.unpack('b', reading)
		outputwriter.writerow([time,x])
		time += timedelta
		reading = inputfile.read(1)	

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

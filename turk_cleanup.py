#!/usr/bin/env python
import os
import re

def csv_cleanup(csv_file, output_file):
	line_count = 0
	
	header_match = re.compile("HitId")
	try:
		output = open(output_file, "wb")
	except Exception as e:
		print("Couldn't open the file: %s" % e)

	first_header = 0

	with open(csv_file, "rb") as f:
		for line in f.readlines():
			if re.search(header_match, line):
				if first_header == 0:
					output.write(line)
					first_header = 1
			else:	
				output.write(line)
				line_count = line_count + 1
	
	print("Number of lines written %d" % line_count)
		

csv_file = "chris_master_turk.csv"
output_file = "master_turk.csv"
csv_cleanup(csv_file, output_file)
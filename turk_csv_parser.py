#!/usr/bin/env python
import csv
import pprint

pp = pprint.PrettyPrinter(indent=4)

# our csv file 
csv_file = "master_turk.csv"


with open(csv_file, 'rb') as csvfile:
	csv_reader = csv.DictReader(csvfile, delimiter=',')
	for row in csv_reader:
		print ("Wish: %s" % (row['Answer 1']))
#!/bin/python3
#
# Class for processing CVS and getting them into the right format to be processed later.
import csv
from host import Host
with open('sample.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in filereader:
        print(row)

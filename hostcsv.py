#!/usr/bin/python3
#
# Class for processing CVS and getting them into the right format to be processed later.
from pathlib import Path as Path
from csv import DictReader as DictReader


class HostCsv:
    def __init__(self, csv_path: Path):
        self.csv_path = csv_path

    def write_csv(self):
        with open(self.csv_path, newline="") as csvfile:
            reader = DictReader(csvfile)
            return [row for row in reader]

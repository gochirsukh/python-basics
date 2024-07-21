#!/usr/bin/python3 
# The script lists out files in a given directory

import os 

directory = '<Directory of your choice>'

for filename in os.scandir(directory):
    if filename.is_file():
        print(filename.path)

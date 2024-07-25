#!/usr/bin/python3
# Citrix client creates .ica files in ~/Download directory and they don't go anywhere. 
# This code removes .ica files in a given directory effortlessly 
# This is just a quick script i wrote under 20 min and it has some room for improvement

import os
import sys

def list_ica(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.ica')]

    if files: 
        print("ICA files in directory")
        for file in files: 
            print(file)            
    else:
        print("No ICA files found")
        sys.exit(0)

def remove_ica(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.ica'):
            file_path = os.path.join(directory, filename)
            try: 
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except:
                print("Something is wrong")

list_ica('/tmp/dumbster')

response = input("Would you like to remove them, y/n: ")

if response.lower() == 'y':
    print("Removing the files")
    remove_ica('/tmp/dumbster')
else:
    print("Answer was no or invalid entry, exit")
    
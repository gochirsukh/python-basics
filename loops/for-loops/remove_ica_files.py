#!/usr/bin/python3
# Removes files with .ica extension in a directory

import os

def remove_ica(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.ica'):
            file_path = os.path.join(directory, filename)
            try: 
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except:
                print("Something is wrong")

remove_ica('/tmp/dumbster')


#!/bin/bash

for line in `cat list.txt`; do 
    mkdir $line
    echo "TBD" > $line/README.md
done



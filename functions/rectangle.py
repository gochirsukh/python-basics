# Simple example for finding aread of rectable 

import sys 


def find_rectangle (length,  width):
    
    if length <= 0 or width <=0:
        print("Length have to be positive number")
        sys.exit(1) 

    rectangle = length * width
    print("The size of rectangle with", "length of", length, "and width of", width, "is", rectangle)


length=int(input("Enter length: "))
print("You have", length, "for length")

width=int(input("Enter width: "))
print("You have", width, "for width")

find_rectangle(length, width)
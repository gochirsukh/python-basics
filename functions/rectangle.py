
import sys 





def find_ractanle(length,  width):
    
    if length <= 0 or width <=0:
        print("Length have to be positive number")
        sys.exit(1) 

    rectancle = length * width
    print("The size of rectanle with", "length of", length, "and width of", width, "is", rectancle)



length=int(input("Enter length: "))
print("You have", length, "for length")

width=int(input("Enter width: "))
print("You have", width, "for width")

find_ractanle(length, width)
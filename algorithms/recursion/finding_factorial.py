def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

num = int(input("Enter a num: "))

if num < 0:
    print("it's negative number. Enter Positive number")
    exit()

print(factorial(num))

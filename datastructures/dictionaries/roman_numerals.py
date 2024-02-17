
myDic = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V"
}
user_input = int(input("Enter number: "))

if user_input > 5:
    print("Value is greater than 5. Enter smaller number")
else:
    print("Roman numeral value of", user_input, "is: ", myDic[user_input])


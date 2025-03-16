# Example of try-except usage

# Custom Exception 1 
class OddNumberError(Exception):
    pass

# Custom Exception 2
class NumberTooLarge(Exception):
    pass

def get_even_number():
    try: 
        num = int(input("Enter an even number less than 10: "))

        if num % 2 != 0:
            raise OddNumberError("It's odd number. Even num please (Error from If statement)")
        if num > 10: 
            raise NumberTooLarge("Number is greater than 10!")
        
        print(f"{num} is valid input!")

    except ValueError: 
        print("Invalid input")
    except OddNumberError as e:     
        print(f"ERROR: {e}")
    except NumberTooLarge as e:
        print(f"ERROR: {e}")
        


get_even_number()
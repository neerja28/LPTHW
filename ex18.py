def print_two(*args):
    arg1, arg2 = args
    print (f"arg1 : {arg1} arg2 :{arg2}")

def print_two_again(arg1, arg2):
    print (f"arg1:{arg1} arg2:{arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("There is nothing here!")

print_two("Neerja","Narayan")
print_two_again("Neerja","Narayan")
print_one("Neerja")
print_none()


# Syntax for function
# 1. Define the function
# 2. Call the function
# def function():

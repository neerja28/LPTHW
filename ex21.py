def add (a,b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract (a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply (a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide (a,b):
    print(f"Dividing {a} / {b}")
    return a / b

age = add (30, 5)
weight = subtract(100, 50)
height = multiply (4, 3)
iq = divide(300, 5)

print (f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

what = add (age, subtract(weight, multiply(height, divide(iq, 2))))
print ("That becomes:", what, "Can you do it by hand?")

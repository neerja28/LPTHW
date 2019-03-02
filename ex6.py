types_of_people = 10
# variable declaration, assigning 10 to types of people
x = f"There are {types_of_people} types of people."
# Using format string indicated by f and {} 

binary = "binary"
# variable declaration, assigning string binary to a variable called binary
do_not = "don't"
# variable declaration, assigning string don't to the variable do_not
y = f"Those who know {binary} and those who {do_not}."
# using format string --> f and {} indicating that the variables in flower brackets needs formatting


print (x)
print (y)

print (f"I said: {x}")
# format string f and {x} 

print (f"I also said '{y}")
# format string f and {y}

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print (joke_evaluation.format(hilarious))
# formatting using .format() for an already created string

w = "This is the left side of .. "
e = " a string with a right side."

print (w + e)
# Concatination of tw strings using +


# Syntax 
# print ("..") ---> prints what's inside the quotes
# print (f"...{}") ---> involves formatting of string by using f  and {}
# print (var.format(some_var)) ---> invovles formatting of string using .format()
# var = "I am {}"
# some_var = "Neerja"
# print (var.format(some_var))
# O/P: I am Neerja
# print (var) ---> prints the value of the variable

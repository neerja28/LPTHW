from sys import argv

script, filename = argv

print (f"We are going to erase the {filename}")
print ("If you don't want that, hit CTRL-C (^C)")
print ("If you do want that, hit RETURN")
input ("?")

print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file...")
# Trucate would delete the contents of the file
target.truncate()

print ("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
# input ('..') would take the input from the user
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write this into a file")

target.write(line1)
# write('stuff') : would write stuff to the file
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print ("And we finally close it.")
# close:  Closes the file
target.close()

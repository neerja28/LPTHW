from sys import argv

script, input_file = argv
# We are using argv since we asking input from the user ie to provide the script and input_file as cmd argument

def print_all(f):
    print (f.read())

current_file = open (input_file)
# We need to first open the file in order to read the file
print_all(current_file)
# we cannot pass the file directly to the function we need to pass the file object
# current_file is the file_object


def rewind(f):
    f.seek(0)

rewind(current_file)
# we are calling rewind function in order to start the file from line1: seek(0) stands for line 1
# current_file is the file object
# current_file passed on as the file object f
# now we can use f in our functions

def print_three_lines(line_count, file):
        print(line_count, file.readline())

print ("Let's print the three lines")

current_line = 1
print_three_lines(current_line, current_file)

current_line = current_line + 1
print_three_lines(current_line,  current_file)

current_line = current_line + 1
print_three_lines(current_line, current_file)

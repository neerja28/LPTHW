from sys import argv
from os.path import exists

script, file1, file2 = argv

print (f"Copying from {file1} to {file2}")

in_file= open(file1)
data_file1 = in_file.read()

print (f"The input file is {len(data_file1)} byets long")

print (f"Does the out file {exists(file2)} exits?")
print("Ready, Hit RETURN to continue, CTRL-C to abort.")
input()

data_file2 = open(file2, 'w')
data_file2.write(data_file1)

print ("Alright, all done")
in_file.close()
file2.close()



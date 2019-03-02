i = 0
numbers  = []
while (i < 6):
    numbers.append(i)
    i = i + 1
    print (numbers)
    print (i)

for num in numbers:
    print (num)

choice = input()

if "0" in choice:
    print ("Got the in part")
if "1" in choice:
    exit(0)
else:
    exit(1)

s = lambda x : x ** 3
print (s(3))

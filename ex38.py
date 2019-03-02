ten_things  = "apples oranges crows tele light sugar"
stuff = ten_things.split(' ')
print (ten_things)

more_stuff = ["Day", "Night","corn","banana","Frisbee","girl","boy"]

while len(stuff) != 10:
    new = more_stuff.pop()
    stuff.append(new)

print (stuff)
stuff.sort()
print(stuff)

print (stuff[1])
print(stuff[-1])


print (' '.join(stuff))
print('#'.join(stuff[3:5]))

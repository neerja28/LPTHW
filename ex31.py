print ("""You are in a dark room with two door. Do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    print ("There's a gaint bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake")
    print("2. Scream at the bear")

    bear = input(">")

    if bear == "1":
        print ("Sorry I was hungry")
    elif bear =='2':
        print ("You took MY cake")
    else:
        print (f"Doing {bear} is probably better to shoo it off")

elif door == "2":
    print ("Welcome to heaven")

else:
    print("Welcome to hell")

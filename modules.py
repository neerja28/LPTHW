"""
mystuff = {"apples" :"I am apple"}
print (mystuff['apples'])

def apple():
    print ("I am apple")


tangerine = "I am an orange"
"""

class Mystuff:

    def __init__(self):
        self.tangerine = "This is an orange"

    def apple(self):
        print ("I am an apple")

thing  =  Mystuff()
thing.apple()
print (thing.tangerine)

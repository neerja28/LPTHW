def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print (f"You have {cheese_count} cheeses!")
    print (f"You have {boxes_of_crackers} boxes_of_crackers!")
    print ("Man that's enough for a party")
    print ("Get a blanket!\n")

print("We can just the numbers directly to the function")
cheese_and_crackers(10, 12)

print ("Or we can pass them as variables")
amount_of_cheese = 20
amount_of_crackers = 30
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print ("We can even do math inside")
cheese_and_crackers(10+20, 30+40)

print ("We can pass it as variables and math")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 200)


# Syntax
# def function(a, b)
# Ways to call this function
# 1. abc =20
#    bca = 40
# function (abc, bca)
# 2. function (10, 20)
# 3. function (abc+30, bca+90)

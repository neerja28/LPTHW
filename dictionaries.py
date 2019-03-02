states = {
'Oregon': 'OR',
'Florida':'FL',
'California':'CA',
'New York': 'NY',
'Michigan':'MI'
}

cities = {
'CA' : 'San Francisco',
'MI' : 'Detroit',
 'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print ('NY has:', cities['NY'])
print("OR had:", cities['OR'])

print ("Michigan abbrevation is:",states['Michigan'])
print ("Florida abbrevation is:", states['Florida'])



for state, abbrev in list(states.items()):
    print (f"{state}========> {abbrev}")


for abbrev,city in list(cities.items()):
    print (f"{abbrev} ========> {city}")


for state, abbrev in list(states.items()):
    print (f"{state} has {abbrev}")
    print (f"{cities[abbrev]}")


state = states.get("Texas")
print (state) # None
if not state:
    print ("Sorry!")


city = cities.get("Texas", "Does not exist")
print (f"The city for Texas is {city}")

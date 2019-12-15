#comparing lists to dictionaries

states = {
'Oregon': 'OR',
'Florida':'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI',
}

#a set of states and cities
cities = {
'CA': 'San francisco',
'MI': 'Detroit',
'FL': 'Jacksonville',
}

#adding some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities

print('-' * 10)

print("New York has: ", cities['NY'])
print("OR has: ", cities['OR'])

#print some states

print('-' * 10)
print("Michigan's abbrevation is: ", states['Michigan'])
print("Florida's abbrevation is: ", states['Florida'])


print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state

print('_' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbervated as {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")


# Now do both at the sametime

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbervated as {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

city = cities.get("'TX', Does not exist")
print(f"The city for the state 'TX' is: {city}")

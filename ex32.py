#for-loops
#
#
the_count = [1, 2, 3, 4, 5, 6]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

#this kind of for-loop goes through the list

for i in the_count:
    print(f"This is the count {i}.")

#fruits

for j in fruits:
    print(f"A fruit type: {j}.")

for k in change:
    print(f"I got {k}.")

#Building empty lists

elements = []

for h in range(0, 6):
    print(f"Adding {h} to the list.")
    elements.append(h)

for h in elements:
    print(f"Printing out Element was: {h}")

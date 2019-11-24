#else if statements

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take all the cars.")
elif cars < people:
    print("We have too many cars.")
else:
    print("We can't make a decision.")


if trucks > cars:
    print("That is too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright let's just take the trucks.")
else:
    print("Fine let's stay home then.")

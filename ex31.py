##writing scripts

print("""
You enter a dark room with 2 doors,
Do you go through Door #1 of Door #2
""")

door = input("> ")

if door == "1":
    print("There is a gaint bear eating a cheese cake.")
    print("what would you do?")
    print("1. Take the cake.")
    print("2. Scream there is a bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats off your face. Good job!")
    elif bear == 2:
        print("The bear eats your leggs off. Good job!!")
    else:
        print(f" Well, doing {bear} is propably better.")
        print("Bear runs away.")
elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survies by the power of jello.")
        print("Good job!!!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!!")
else:
    print("You stumble around and fall on a knife and die. Good job!!!")

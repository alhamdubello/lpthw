#functions and variables
#
#
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese.")
    print(f"You have {boxes_of_crackers} box of crackers.")
    print("Man that is enough for the party!!!")
    print("Get a blanket.\n")

print("We can just give funtion numbers directly: ")
cheese_and_crackers(20,30)

print("Or we can use variables from our scripts:")
amount_of_cheese = 10
amount_of_crackers = 50


cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside:")
cheese_and_crackers(10+20,5+6)

print("We can combine two variable and math together:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

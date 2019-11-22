#Names, variables, code, functions
#
#This will really be intersting doing this for the first time for ne
#
#
#

#This is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#we can just do it in a slightly different way

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument

def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments

def print_no_args():
    print("I got nothing.")



print_two("Alhamdu", "Bello")
print_two_again("Zahra", "Alhamdu")
print_one("baby Zahra")
print_no_args()    

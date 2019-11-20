#I am now working on variables and names
#This is part of exercise 4
#
#assign a car the value of 100
cars = 100
#assign space_in_a_car a float value of 4.0
space_in_a_car = 4.0
#assign drivers a value of 30
drivers = 30
#assing passengers a value of 90
passengers = 90
#assign to variable cars_not_driven = cars - drivers
cars_not_driven = cars - drivers
#assign drivers to a new variable
cars_driven = drivers
#multiply driven cars by space in a car assign value to new variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
#find the average number of passenges per car
average_passengers_per_car = passengers / cars_driven
#
#
#Now print out the answers

print("Thers are", cars, "cars available.")

print("There are only", drivers, "drivers available.")

print("There will be", cars_not_driven, "empty cars today.")

print("We can transport", carpool_capacity, "people today.")

print ("We have", passengers, "to carpool today.")

print("We need to put about", average_passengers_per_car, "in each car.")

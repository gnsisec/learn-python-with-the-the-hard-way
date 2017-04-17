#This is Python version 2.7.12
#Exercise 4: Variables And Names

#Total available cars
cars = 100

#Cars Size
space_in_a_car = 4.0

#Total drivers available
drivers = 30

#Total passegers
passegers = 90

########## Calculate ##########
#Total idle cars
cars_not_driven = cars - drivers

#Total standby cars
cars_driven = drivers

#Total area for cars
carpool_capacity = cars_driven * space_in_a_car

#Average capacity in car
average_passegers_per_car = passegers / cars_driven


print "There are", cars, "available"
print "There are only", drivers, "available"
print "There will be", cars_not_driven, "empty cars"
print "We can transport", carpool_capacity, "per day"

print "\nToday Calculation"
print "We have %d carpool today" % passegers                          #Add some tricky to print in other way
print "We need to put about", average_passegers_per_car, "each car"

#This is Python version 2.7.12
#Exercise 19: Functions and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for party!"
    print "Get a blanket.\n"

print "We can just give the function number direcly:"
cheese_and_crackers(20,30)

print "Or, we can use variables from our script:"
amount_of_chesse = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_chesse, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variable and math:"
cheese_and_crackers(amount_of_chesse + 100, amount_of_crackers + 1000)

print "Add some input:"
amount_of_chesse = input("How many cheese? ")
amount_of_crackers = input("How many rackers? ")
cheese_and_crackers(amount_of_chesse, amount_of_crackers)

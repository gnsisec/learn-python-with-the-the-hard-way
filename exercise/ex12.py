# This is Python version 2.7.12
# Exercise 12: Prompting People

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = int(raw_input("How much do you weight? "))

print "So, you're %r old, %s tall and %d heavy" % (
    age, height, weight)

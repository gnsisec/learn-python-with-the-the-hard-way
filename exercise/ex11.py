# This is Python version 2.7
# Exercise 11: Asking Questions

# using raw_input with convert to integer
print "How old are you?",
age = int(raw_input())

# using raw_input
print "How tall are you?",
height = raw_input()

# Using input()
print "How much do you weight?",
weight = input()

print "So, you're %r old, %r tall and %r heavy" % (
    age, height, weight)

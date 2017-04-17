#This is Python version 2.7.12
#Exercise 23: Read Some Code

from math import factorial, sqrt

x = input("Input factorial number   : ")
y = input("Input pow number         : ")

new_x = factorial(x)
new_y = sqrt(y)
print "Factorial %i: %i" % (x, new_x)
print "Pow %i: %i" % (y, new_y)

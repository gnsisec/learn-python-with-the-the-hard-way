#This is Python version 2.7.12
#Exercise 13: Parameters, Unpacking, Variables

# to run this use:
# python ex13.py fly with wings

from sys import argv

script, first, second, third = argv

fourth = raw_input("Big or Small ?             ")

print "\nThe script is called     :", script
print "Your first variable is   :", first
print "Your second variable is  :", second
print "Your third variable is   :", third

#combine input from user and arguments
print "\nI am " + first + "ing with" + " %s" %(fourth), third

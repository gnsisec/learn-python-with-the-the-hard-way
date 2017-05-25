# This is Python version 2.7.12
# Exercise 15: Reading Files

# to run this use:
# python ex15.py ex15_sample.txt

from sys import argv

script, filename = argv

# open file ex15_sample.txt from argument
txt = open(filename)

# print text in ex15_sample.txt
print "Here's your file %r" % filename
print "\n" + txt.read()
txt.close()

# input again file ex15_sample.txt
print "\n\nType the filename again:"
file_again = raw_input("> ")

# then print again text ex15_sample.txt
txt_again = open(file_again)
print "\n" + txt_again.read()
txt.close()

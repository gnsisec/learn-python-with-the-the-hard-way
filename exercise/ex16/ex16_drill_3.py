# This is Python version 2.7
# Exercise 16: Reading and Writing Files

# to run this use:
# python ex16.py test.txt

# Drill 3
'''
There's too much repetition in this file.
Use strings, formats, and escapes to print out
line1, line2, and line3 with just one target.write()
command instead of six.
'''

from sys import argv

script, filename = argv

# Truncate all data Here
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")

print "\nOpening the file..."
target = open(filename, 'w')
print "\nTruncating the file. Goodbye!"
target.truncate()

# Add 3 line sentences
print "\nNow I'm going to ask you three line."
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

# Write the 3 sentences to file
print "\n\t\t\tI'm going to write these to the file."
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# Close the file
print "\t\t\tAnd finally, we close it.\n"
target.close()

# Open and read test.txt first
print "\nWe're going print %r." % filename
target = open(filename, 'r')
print target.read()

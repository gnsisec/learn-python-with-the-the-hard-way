# This is Python version 2.7.12
# Exercise 17: More Files

# to run this use:
# python ex17.py test.txt new_file.txt

# Drill 2:
# See how short you can make the script.
# I could make this one line long.

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how ?
# in_file = open(from_file)
# indata = in_file.read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort"
# raw_input()

# out_file = open(to_file,'w')
open(to_file, 'w').write(open(from_file).read())

# print "Alright, all done"

# out_file.close()
# in_file.close()
# information:
'''
When I try to make this script shorter I get an error when I close the files at the end.
You probably did something like this, indata = open(from_file).read(),
which means you don't need to then do in_file.close()
when you reach the end of the script.
It should already be closed by Python once that one line runs.
'''

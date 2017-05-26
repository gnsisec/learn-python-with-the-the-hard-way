# This is Python version 2.7
# Exercise 23: Read Some Code

import datetime

now = datetime.datetime.now()

print
print "Current date and time using str method of datetime object"
print str(now)

print
print "Current date time using instance attributes."
print "Current year             : %d" % now.year
print "Current month            : %d" % now.month
print "Current day              : %d" % now.day
print
print "Current hour             : %d" % now.hour
print "Current minute           : %d" % now.minute
print "Current second           : %d" % now.second
print "Current miliseconnd      : %d" % now.microsecond

print
print "Current date and time using strftime:"
print now.strftime("%Y-%m-%d %H:%M")

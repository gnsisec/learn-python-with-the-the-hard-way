# This is Python version 2.7.12
# Exercise 23: Read Some Code

from datetime import datetime

now = datetime.now()

mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)

print "Date:",
print mm + "/" + dd + "/" + yyyy

print "Time:",
print hour + ":" + mi + ":" + ss

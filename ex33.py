#This is Python version 2.7.12
#Exercise 33: While Loops

i = 0
numbers = []

while i < 6 :
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Number now: ", numbers
    print "At the bottom i is %d" % i
    print

print "\nThe numbers: "

for num in numbers:
    print num

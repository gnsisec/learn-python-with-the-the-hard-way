#This is Python version 2.7.12
#Exercise 6: Strings and Text

x = "There are %d types of people" % 10
binary  = "binary"
do_not = "don't"
y = "Those know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

##########True or False##########
hilarious = False
joke_evalutation = "\nIsn't that joke so funny?! %r"
print joke_evalutation % hilarious

##########Join the string##########
w = "\nThis is the left side of..."
e = "a string with right side."
print w + e

# This is Python version 2.7.12
# Exercise 23: Read Some Code

# must declare default in left


def bio(status, age, name="Budi"):
    print "Your name    : %s" % name
    print "Your age     : %s" % age
    print "Your status  : %s" % status
    print
    return


bio("single", 17)
bio("double", 17, "Jaka")
bio(status="double", age=17, name="Dono")

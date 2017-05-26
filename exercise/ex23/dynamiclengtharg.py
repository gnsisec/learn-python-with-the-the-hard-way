# This is Python version 2.7
# Exercise 23: Read Some Code


def create(*vartuple):
    print "Output is :",
    # print vartuple
    for i in vartuple:
        print i,
    print "\n"
    return i


create(10)
create(40, 20)
create(90, 80, 20)

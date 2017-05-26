# This is Python version 2.7
# Exercise 18: Names, Variables, Code, Functions

# this one is like your scripts with argv


def print_two(*args):
    arg1, arg2, arg3, arg4 = args
    print "arg1 : %r, arg2 : %r, arg3 : %r, arg4 : %r" \
        % (arg1, arg2, arg3, arg4)


# ok, that *args is actually pointless, we can just do This
def print_two_again(arg1, arg2):
    print "arg1 : %r, arg2 : %r" % (arg1, arg2)


# this just take one argument
def print_one(arg1):
    print "arg1: %r" % arg1


# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed", "Shaw", "More", "Ball")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

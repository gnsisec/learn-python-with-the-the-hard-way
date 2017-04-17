#This is Python version 2.7.12
#Exercise 23: Read Some Code

#global variable
total = 0

# Function definition is here
def sum (arg1, arg2):
    # Add both the parameters and return them.
    total = arg1 + arg2
    print "Inside the function      : ", total
    return total

# Now you can call sum function
sum(10,20);
print "Outside the function     : ", total

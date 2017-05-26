# This is Python version 2.7
# Exercise 23: Read Some Code

import random

min=1
max=6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y" or roll_again == "YES":
    print "Roll The Dice!!!"
    print "You got", random.randint(min, max), "in first dice"
    print "You got", random.randint(min, max), "in second dice\n"
    roll_again = raw_input("Do you want roll again? (yes/no) ")
    print

print "###################################"
print "### Thanks for rolling the dice ###"
print "###################################"

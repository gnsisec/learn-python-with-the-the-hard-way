#This is Python version 2.7.12
#Exercise 39: Dictionaries, Oh Lovely Dictionaries - MORE!!!

#Print Function
def for_print(items):
    for a,b in box.items():
        print "Slot number %s is %s." % (a, b)

#Initiate Dict
box = {
    1: 'Knife',
    2: 'Molotov'
}

#For print all in dictionary
for_print(box)

#Change value in there then print again
box [1] = 'Bubbles'
print "\nI change box %s with %s" % (1,'Bubbles')
for_print(box)

#for get value, but we can return any false data if not exist
print box.get(4,'Doesn\'t exist')

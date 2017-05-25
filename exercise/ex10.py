# This is Python version 2.7.12
# Exercise 10: What Was That?

# Escape The F*ckin error
# print "I am 6'2\" tall."
# print 'I am 6\'2" tall'
# tricks put \ in front of the quotes that you use to print.

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat with %r"

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat % (fat_cat)
print fat_cat

# Dont Active this code! INFINITE LOOPING!
# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" % i,

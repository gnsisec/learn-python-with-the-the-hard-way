#This is Python version 2.7.12
#Exercise 5: More Variables and Printing

my_name = 'Matthew Christian'
my_age = 25         # not a lie in 2017
my_height = 178     # cm
my_weight = 66      # kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s"         % my_name

print "He's %d centimeter tall or %r inch"     % (my_height, round((my_height * 0.393701)))
print "He's %d kilogram heavy or %r pounds"      % (my_weight, round((my_weight * 2.20462)))
print "Actually that's not too heavy LOL"
print "He's got %s eyes and %s hair"    % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee"    % my_teeth

print "\nIf I add %d, %d and %d I get %r" % (my_age, my_height, my_weight, my_age + my_height + my_weight)

#This is Python version 2.7.12
#Exercise 14: Prompting and Passing

# to run this use:
# python ex14.py matthew

# 2. Change the prompt variable to something else entirely.
# 3. Drill: Add another argument and use it in your script,
# the same way you did in the previous exercise with first, second = ARGV.

from sys import argv

script, user_name, status = argv
prompt = 'answer: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you few questions."
print "Do you like me %s ?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r compter. Nice.
Your status %r.
""" % (likes, lives, computer, status)

# This is Python version 2.7
# Exercise 44: Inheritance Versus Composition


class Other(object):

    def override(self):
        print "OTHER override()\n"

    def implicit(self):
        print "OTHER implicit()\n"

    def altered(self):
        print "OTHER altered()\n"


class Child(object):

    def __init__(self):
        self.composition = Other()

    def implicit(self):
        self.composition.implicit()

    def override(self):
        print "CHILD override()\n"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.composition.altered()
        print "CHILD, AFTER OTHER altered()"


son = Child()

son.implicit()
son.override()
son.altered()

# This is Python version 2.7.12
# Exercise 44: Inheritance Versus Composition


class Parent(object):

    def override(self):
        print "PARENT override()\n"

    def implicit(self):
        print "PARENT implicit()\n"

    def altered(self):
        print "PARENT altered()\n"


class Child(Parent):

    def override(self):
        print "CHILD override()\n"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        # super(Child, self).altered()
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()\n"


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

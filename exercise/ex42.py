# This is Python version 2.7.12
# Exercise 42: Is-A, Has-A, Objects, and Classes

# Animal is-a object (yes, sort of confusing) look at the extra credit


class Animal(object):
    pass

# class named Dog is-a Animal


class Dog(Animal):

    def __init__(self, name):
        # class named Dog has-a __init__ function that takes self and \
        name parameters
        self.name = name


# class named Cat is-a Animal

class Cat(Animal):

    def __init__(self, name):
        # class named Cat has-a __init__ function that takes self and \name parameters
        self.name = name

# class named Person is-a object


class Person(object):

    def __init__(self, name):
        # class named Person has-a __init__ function that takes self and name parameters
        self.name = name

        # Person has-a pet of some kind
        self.pet = None


# class named Employee is-a Person


class Employee(Person):

    def __init__(self, name, salary):
        # ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        # ??
        self.salary = salary

# class named Fish is-a Object


class Fish(object):
    pass

# class named Salmon is-a Fish


class Salmon(Fish):
    pass

# class named Halibut is-a Fish


class Halibut(Fish):
    pass
    # rover is-a Dog
    rover = Dog("Rover")

    # satan is-a Cat
    satan = Cat("Satan")

    # mary is-a Person
    mary = Person("Mary")

    # mary.pet has-a satan
    mary.pet = satan

    # frank is-a Employee("Frank", 120000)
    frank = Employee("Frank", 120000)

# frank.pet has-a rover


failrank.pet = rover
# flipper is-a Fish
flipper = Fish()
# crouse is-a Salmon
crouse = Salmon()
# harry is-a Halibut
harry = Halibut()

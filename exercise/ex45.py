# This is Python version 2.7.12
# Exercise 45: You Make A Game


class game(object):
    def __init__(self):
        self.level_one = level_one()
        self.level_two = level_two()

    def start(self):
        self.level_one.enter()
        self.level_two.enter()


class mission(object):
    def welcome(self):
        print "Welcome Your are in mission level %s" % (self.level)

    def success(self):
        print "Success finish level %s\n" % (self.level)

    def fail(self):
        print "You failed at level %s\n" % (self.level)
        exit(1)

    def finish(self):
        print "Congrats! You finish it!!!"
        exit(0)


class level_one(mission):
    def enter(self):
        self.level = 1
        self.welcome()

        action = raw_input("If I have 4 Cake, and My sister eat 2. \nHow many cakes that I have after that ? ")
        if action == "2":
            self.success()
        else:
            self.fail()


class level_two(mission):
    def enter(self):
        self.level = 2
        self.welcome()

        action = raw_input("How many days in a year? ")
        if action == "365":
            self.success()
            self.finish()
        else:
            self.fail()


play = game()
play.start()

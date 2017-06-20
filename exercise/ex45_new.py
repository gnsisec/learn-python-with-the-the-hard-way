class level():
    def level_one(self):
        print "###      This is Level one       ###"
        self.math_one = input("Give me number 6 * 2: ")
        if self.math_one == 12:
            print "You are right!\n"
        else:
            print "You are  wrong!\n"
            exit(0)

    def level_two(self):
        print "###      This is Level two       ###"
        self.math_two = input("Give me number 8 / 2: ")
        if self.math_two == 4:
            print "You are right!\n"
        else:
            print "You are  wrong!\n"
            exit(0)

    def level_three(self):
        print "###      This is Level three     ###"
        self.math_three = input("Give me number 10 - 5: ")
        if self.math_three == 5:
            print "You are right!\n"
        else:
            print "You are  wrong!\n"
            exit(0)


class game():
    def __init__(self):
        self.mission = level()

    def play(self):
        print "###      Welcome To XXX Game     ###\n\n"

        self.mission.level_one()
        self.mission.level_two()
        self.mission.level_three()

        print "######################################"
        print "###      You Complete The Game     ###"
        print "######################################"


game = game()
game.play()

#This is Python version 2.7.12
#Exercise 36: Designing and Debugging

from sys import exit

def main():
    print "Choose Paper/Rock/Scissor"
    play = raw_input("> ")
    check(play)

def check(item):
    if item == "Paper" or item == "paper":
        win("You choose "+item+" !")
    elif item == "Rock" or item == "rock":
        dead("You choose "+item+" !")
    elif item == "Scissor" or item == "scissor":
        dead("You choose "+item+" !")
    else:
        dead("Why not choose a correct option ?")

def win(success):
    print success,"You win!!!"
    exit(0)

def dead(fool):
    print fool,"GAME OVER!!!"
    exit(0)

main()

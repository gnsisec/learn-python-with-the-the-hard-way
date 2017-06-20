'''Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can
escape into an escape pod to the planet below. The game will be more like a Zork or Adventure type game with
text outputs and funny ways to die. The game will involve an engine that runs a map full of rooms or scenes.
Each room will print its own description when the player enters it and then tell the engine what room to run
next out of the map.'''

# * Map
#   - next_scene
#   - opening_scene

# * Engine
#   - play

# * Scene
#   - enter
#   * Death
#   * Central Corridor
#   * Laser Weapon Armory
#   * The Bridge
#   * Escape Pod

from sys import exit
from random import randint

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.get_scene(self.scene_map.start_scene)
        last_scene = self.scene_map.get_scene('finished')
        print 'start screen engine in ', current_scene
        print 'ending screen engine in ', last_scene

        while current_scene != last_scene:

            # run the scene and return the next scene
            return_next_scene = current_scene.enter()

            # trasnform Map into a Scene
            current_scene = self.scene_map.get_scene(return_next_scene)

        # to finished move!!!
        current_scene.enter()


class Scene(object):
    def enter(self):
        print "This scene is not yet configure. Subclass it and implement enter()."
        exit(1)


class Death(Scene):
    quips = [
        "You died.  You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
        ]

    def enter(self):
        print "\nYou DIED!"
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print "\nChoose it:"
        print "a. shoot!"
        print "b. dodge!"
        print "c. tell a joke"
        action = raw_input("> ")

        if action == "shoot!":
            return 'death'
        elif action == "dodge!":
            return 'death'
        elif action == "tell a joke":
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return 'central_coridor'


class EscapePod(Scene):
    def enter(self):
        print "\nGuest Number: "
        good_pod = randint(1, 5)
        print good_pod
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            return 'death'
        else:
            return 'finished'


class Finished(Scene):
    def enter(self):
        print "\nYou won! Good job."
        return 'finished'

    # Hmmm I think we dont need this anymore!!!
    # Why need opening scene if it only tranform the map into a scene?!
    # def opening_scene(self):
    #     return self.next_scene(self.start_scene)


class Map(object):
    scenes = {
        'central_coridor': CentralCorridor(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def get_scene(self, scene_name):
        scene = Map.scenes.get(scene_name)
        return scene


the_map = Map('central_coridor')
# print "set start map: " + the_map.start_scene + "\n"

# the_game = Engine(the_map)  # the_map.start_scene
# # print "set start engine in: " + the_game.scene_map.start_scene + "\n"
#
# the_game.play()

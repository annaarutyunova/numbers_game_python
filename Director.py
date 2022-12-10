from time import sleep
import Player
import Number
# Before adding the 2 lines below it was giving the following error "Traceback (most recent call last):
#   File "d:\School\Applied Programming\numbers_game_python\Director.py", line 6, in <module>
#     class Director():
#   File "d:\School\Applied Programming\numbers_game_python\Director.py", line 7, in Director
#     player = Player()
# TypeError: 'module' object is not callable"
from Player import *
from Number import *


class Director():
    player = Player()
    number = Number()
    numbersEntered = ""
    time = 2000
    ifMatch = True

    def __init__(self):
        # StartGame()
        # Play()
        pass

    def WelcomeMessage(self):
        print("This is a memory game. A set of numbers will be displayed. You have a couple of seconds to memorize them. Once they dissapear, you will be asked to enter the numbers you saw on the screen a moment eariler. As long as you get them right, you will be given a longer sequence of numbers each time. If you get it wrong once, you will be asked if you want to start the gameover. Once you are ready, press Enter. If you want to exit press ctrl C")
        # input()
    
    def EnterNumbers(self):
        print("What were the numbers? Don't include any spaces or commas")
        print()
        Director.numbersEntered = input
        print()

    def GetNumbersEntered(self):
        # return Director.numbersEntered
        print(Director.numbersEntered)

    def Compare(self, a, b):
        if a == b:
            print("You got it right!")
            return Director.ifMatch
        else:
            print("Oops")
            print()
            return Director.ifMatch == False
    def StartGame(self):
        Director.WelcomeMessage(self)
        Number.number.MakeNumberSequence()
        Number.number.PrintNumbers()

    def Clear(self):
        # threading.sleep(Director.time)
        sleep(Director.time)
        print()

c = Director()
c.WelcomeMessage()
# c.EnterNumbers()
# c.GetNumbersEntered()
c.Clear()

# Questions
# sortof got fixed when "from Player import *" Run this code and fix the error. How do I acces other classes in this class? I need a Player and a Number
# How do I use methods from other classes in instances of those classes here? Like number.MakeNumberSequence
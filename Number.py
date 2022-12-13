import random

class Number:
    nums = ""

    def __init__(self):
        pass

    def GenerateRandomNumber(self):
        return random.randint(1,9)
 
    def MakeNumberSequence(self):
        for i in range(4):
            a = Number.GenerateRandomNumber(self)
            Number.nums = Number.nums + str(a)
            i += 1
        print(Number.nums)
    
    def AddToNumberSequence(self):
        for i in range (2):
            a = Number.GenerateRandomNumber(self)
            Number.nums = Number.nums + str(a)
            i += 1

    def PrintNums(self):
        # a = " ".join(Number.nums)
        a = Number.nums
        print(a)

    def Clear(self):
        print()

    def ClearNums(self):
        Number.nums = ""
        



import random

class Number:
    # numbers = []
    nums = ""

    def _init__(self):
        pass

    def GenerateRandomNumber(self):
        return random.randint(1,9)

    # def MakeNumberList(self):
    #     for i in range(4):
    #         # i = Number.GenerateRandomNumber(self)
    #         Number.numbers.append(Number.GenerateRandomNumber(self))
    # def AddToNumberList(self):
    #     for i in range (2):
    #         Number.numbers.append(Number.GenerateRandomNumber(self))
    #         i += 1
    # def PrintNumbers(self):
    #     for i in Number.numbers:
    #         print(i, end=" ") 
    # def Clear(self):
    #     print()
    # def ClearList(self):
    #     Number.numbers.clear()
    #     print("The list is empty")

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
        print(Number.nums)

    def PrintNums(self):
        a = " ".join(Number.nums)
        print(a)
    def Clear(self):
        print()
    def ClearNums(self):
        Number.nums = ""
        if len(Number.nums) == 0:
            print("There are no numbers ")
        else:
            print("You did not clear the string")



x = Number()
# x.GenerateRandomNumber()
# x.MakeNumberList()
# x.AddToNumberList()
# x.PrintNumbers()
# x.ClearList()

# x.MakeNumberSequence()
# x.AddToNumberSequence()
# x.PrintNums()
# x.ClearNums()
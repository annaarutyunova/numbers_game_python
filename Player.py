
class Player():
    numbersSeen = []
    numbers = ""

    def __init__(self):
        pass
    
    # def GetNumbers(self, userinput = "hel lo  "):
    #     t = userinput.strip()
    #     print(f'After split it is {t}')
    #     t.replace(" ", "")
    #     Player.numbersSeen.append(t.split())
    #     # return Player.numbersSeen
    #     print (len(Player.numbersSeen))
    # def Hello(self):
    #     print("hello")

    def GetNumbers(self, userinput = "hel lo"):
        t = userinput.strip()
        print(t)
        t = t.replace(" ", "")
        print(t)

    

# a = Player()
# a.GetNumbers()
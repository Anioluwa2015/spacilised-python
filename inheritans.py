class mom:
    def __init__(self,eye,country):
        self.eye = eye
        self.country = country
    def display(self):
        print("my name is",self.name)
        print("your favorite game is",self.game)
        print("you will be",self.age)
        print("you have", self.eye)
        print("you are born in", self.country)
    
    
class Ani(mom):
    def __init__(self,name,game,age,eye,country):
        self.name = name
        self.game = game
        self.age = age
        super().__init__(eye,country)
a1 = Ani("Ani" , "toca boca" ,"10 in few weeks","brown","nigeria")
a1.display()
print(issubclass(Ani , mom))
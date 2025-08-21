class games():
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def display(self):
        print(self.name,"is my favorite game and it has ", self.type)
games1=games('toca life world', 'lots of location and adventures')
games1.display()
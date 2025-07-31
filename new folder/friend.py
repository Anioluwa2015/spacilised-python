class Friend:
    def __init___(self,name,colour):
        self.name=name
        self.colour=colour
    def intro(self):
        print("My friend's name is ", self.name," and her favorite color is ", self.colour)
Shaza=Friend("Shaza","Purple")
Ani=Friend("Ani","blue")
Shaza.intro()
Ani.intro()
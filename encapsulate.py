class games: 
    __var = 'hello kitty and toca life world '
    def __init__(self,name,rating,types):
      self.name=name
      self.rating=rating
      self.type=types
    def display(self):
      print("My favorite game is" , self.name ,"And my rating of this game is", self.rating,". It is a" , self.types)
obj = games("hello kitty",8,"adventure and discovery")
obj.display
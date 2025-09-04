class games: 
    __var = 'toca life world '
    def __init__(self,name,rating,types):
      self.name=name
      self.rating=rating
      self.types=types
    def display(self):
      print("My favorite game is" , self.name ,"And my rating of this game is", self.rating,". It is a" , self.types)
obj = games("toca boca",9,"adventure and discovery")
obj.display
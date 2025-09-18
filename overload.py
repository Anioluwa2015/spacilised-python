class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def add_points(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    
p1 = Point(3, 3)
p2 = Point(3, 3)

p3 = p1.add_points(p2)

print((p3.x, p3.y)) 
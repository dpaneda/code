from math import pow, sqrt

class coord:
        def __init__(self,x,y,z):
                self.x = x
                self.y = y
                self.z = z
        def tuple(self):
                return (self.x,self.y,self.z)
        def __add__(self, c):
                return coord (self.x + c.x, self.y + c.y, self.z + c.z)
        def __sub__(self, c):
                return coord (self.x - c.x, self.y - c.y, self.z - c.z)
        def dist(self, c):
                aux =  c-self
                return sqrt(pow(aux.x,2) + pow(aux.y,2) + pow(aux.z,2))

a = coord(2,2,2)
b = coord(1,1,2)

print a.dist(b)


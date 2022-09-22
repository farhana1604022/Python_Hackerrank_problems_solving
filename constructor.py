import math

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def norm(self):  
        n=math.sqrt(self.x**2+self.y**2)
        return n
    
p=Point(2.0,3.0)
print(p.x,p.y,p.norm()) 
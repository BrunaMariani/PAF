import math
class Particle:
    def __init__(self, mass, x_0):
        self.mass = mass
        self.x_0 = x_0 
    def printInfo(self):
        print(f'Čestica ima masu {self.mass:.2f} i u početnom trenutku se nalazi na polozaju x = {self.x_0:.2f}')
    def udaljenost(self):
        d = math.fabs(self.x_0)
        print(d)
    def udaljenost2(self,x_k):
        d = x_k - self.x_0 
        d = math.fabs(d)
        print(d)

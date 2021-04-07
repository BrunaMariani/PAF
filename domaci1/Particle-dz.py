from math import sin,cos,radians, sqrt
import matplotlib.pyplot as plt
class Particle:
    def __init__(self, v0, theta, x0, y0):
        self.v0 = v0
        self.theta = radians(theta)
        self.x = x0
        self.y = y0
        self.x_ = []
        self.y_ = []
        self.x_.append(x0)
        self.y_.append(y0)
        self.vx = v0*cos(self.theta)
        self.vy = v0*sin(self.theta)
        self.t = 0
        self.vy_ = []
    
        
    def printInfo(self):
        print(f'{self.v0},{self.theta},{self.x},{self.y}')
    def reset(self):
        self.v0 = 0
        self.theta = 0
        self.x0 =0
        self.y0 = 0
        self.y_ = []
        self.x_ = []
        self.vy_ = []
    
        
    def __move(self, dt):
        g = 9.81
        self.x = self.x + self.vx*dt
        self.vy = self.vy - g*dt
        self.y = self.y + self.vy*dt
        self.x_.append(self.x)
        self.y_.append(self.y)
        self.vy_.append(self.vy)
   
    
    
    def total_time(self,dt):
        while True:
            self.__move(dt)
            self.t += dt
            if self.y <= 0:
                break
        return self.t
    def max_brzina(self,dt):
        while True:
            self.__move(dt)
            if self.y <= 0:
                break
        v_ymax = max(abs(self.vy_))
        v_max = sqrt(v_ymax**2+self.vx**2)
        print(v_max)
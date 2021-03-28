from math import sin,cos,radians
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
        
    def printInfo(self):
        print(f'{self.v0},{self.theta},{self.x},{self.y}')
    def reset(self):
        self.v0 = 0
        self.theta = 0
        self.x0 =0
        self.y0 = 0
        self.y_ = []
        self.x_ = []
    
    def __move(self, dt):
        g = 9.81
        self.x = self.x + self.vx*dt
        self.vy = self.vy - g*dt
        self.y = self.y + self.vy*dt
        self.x_.append(self.x)
        self.y_.append(self.y)
    def range(self):
        x = self.x
        while True:
            self.__move(0.1)
            if self.y <= 0:
                break
        
        print(self.x-x)
    
    def plot_trajectory(self):
        plt.plot(self.x_,self.y_)
        plt.show()
        
        



       
        

        
            
            
        

       
        

        
       

       

    
        
             
      
            








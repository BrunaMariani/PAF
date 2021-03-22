from math import sin,cos,radians
class Particle:
    def __init__(self, v0, theta, x0, y0):
        self.v0 = v0
        self.theta = theta
        self.x0 = x0
        self.y0 = y0
        self.x_ = []
        self.y_ = []
    def printInfo(self):
        print(f'{self.v0},{self.theta},{self.x0},{self.y0}')
    def reset(self):
        self.v0 = 0
        self.theta = 0
        self.x0 =0
        self.y0 = 0
    
    def __move(self, dt):
        g = 9.81
        y = self.y0
        x = self.x0
        theta = radians(self.theta)
        v_x = self.v0 * cos(self.theta)
        x = self.x0 + v_x * dt
        v_y = self.v0*sin(self.theta)
        v_y = v_y - g*dt
        y =  self.y0 + v_y*dt
        self.x_.append(x)
        self.y_.append(y)
       
        
       

       

    def range(self):
        self.__move(0.5)
             
        print(x)
             
      
            

p1 = Particle(30,45,2,2)
p1.printInfo()
p1.range()






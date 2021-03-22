from math import sin,cos,radians
class Particle:
    def __init__(self, v0, theta, x0, y0):
        self.v0 = v0
        self.theta = theta
        self.x0 = x0
        self.y0 = y0
        self.x_ = []
        self.y_ = []
        self.y = 0
        self.x = 0
    def printInfo(self):
        print(f'{self.v0},{self.theta},{self.x0},{self.y0}')
    def reset(self):
        self.v0 = 0
        self.theta = 0
        self.x0 =0
        self.y0 = 0
    
    def __move(self, dt):
        g = 9.81
        
        
    
        theta = radians(self.theta)
        v_x = self.v0 * cos(self.theta)
        self.x = self.x0 + v_x * dt
        v_y = self.v0*sin(self.theta)
        v_y = v_y - g*dt
        self.y =  self.y0 + v_y*dt
        self.x_.append(self.x)
        self.y_.append(self.y)
    def range(self):
       
        

        
            
            
        

       
        

        
       

       

    
        
             
      
            
p1 = Particle(30,45,2,2)
p1.printInfo()
p1.range()







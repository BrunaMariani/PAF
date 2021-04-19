import math
import matplotlib.pyplot as plt
class VertikalniHitac:
    def __init__(self,y0,v0):
        self.y = y0
        self.v = v0
        self.y_ = []
        self.v_ = []
        self.t = 0
        self.t_ = []
        self.y_.append(self.y)
        self.v_.append(self.v)
        self.t_.append(self.t)
    
    def printInfo(self):
        print(f'Objekt je uspjesno stvoren, početna je visina {self.y}, a brzina {self.v}')
    
    def promijena_visine(self,y):
        self.y = y
    def promijena_brzine(self,v):
        self.v = v
    def vertikalni_hitac(self,dt):
        g=9.81
        while True:
            self.v = self.v - g*dt
            self.y = self.y + self.v*dt
            self.t+= dt
            if self.y <= 0:
                break
            self.y_.append(self.y)
            self.v_.append(self.v)
            self.t_.append(self.t)
        return self.y_,self.v_,self.t_
    def maks_visina(self,dt):
        g = 9.81
        while True:
            self.v = self.v - g*dt
            self.y = self.y + self.v*dt
            if self.v <=0:
                break
        return(self.y)

    def vrijeme(self,dt):
        self.vertikalni_hitac(dt)
        t = self.t_[-1]
        return(t)
    def otpor(self,dt,k,m):
        g = 9.81
        F = -k*self.v
        a = (-1*m*g-k*self.v)/m
        while True:
            self.v = self.v + a*dt
            self.y = self.y + self.v*dt
            self.t+= dt
            if self.v >= 0:
                a = (-m*g-k*self.v)/m
            else:
                a = (m*g-k*self.v)/m

            if self.y <= 0:
                break
            self.y_.append(self.y)
            self.v_.append(self.v)
            self.t_.append(self.t)

        return self.y_,self.v_,self.t_
   
#p = VertikalniHitac(1,30)
#p.printInfo()
#p.vertikalni_hitac(0.01,5)
#p.maks_visina(0.01)
#p.vrijeme(0.01)
#p.otpor(0.01,2,5)

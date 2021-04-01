import math
import matplotlib.pyplot as plt
class HarmonicOscilator:
    def __init__(self,k,m,x0,v0):
        self.x_l = []
        self.v_l = []
        self.a_l = []
        self.t_l = []
        self.k = k
        self.m = m
        self.x = x0
        self.v = v0
        self.a = 0
        self.t = 0

    def oscillate(self,dt,t):
        N = int(t/dt)
        for i in range(N):
            self.a = -(self.k*self.x)/self.m
            self.v = self.v + self.a*dt
            self.x = self.x + self.v*dt
            self.t += dt
            self.x_l.append(self.x)
            self.v_l.append(self.v)
            self.a_l.append(self.a)
            self.t_l.append(self.t)
        return self.x_l,self.v_l,self.a_l,self.t_l

    def plot_trajectory(self,dt,t):
        x,v,a,t = self.oscillate(dt,t)
        plt.subplot(1,3,1)
        plt.plot(t,x)
        plt.subplot(1,3,2)
        plt.plot(t,v)
        plt.subplot(1,3,3)
        plt.plot(t,a)
        plt.show()
h1 = HarmonicOscilator(10,0.1,0.3,0)
h1.plot_trajectory(0.01,2)

import matplotlib.pyplot as plt
from math import sin, cos, radians
def jednoliko_gibanje(F,m,t):
    a = F/m
    d_t = 0.5
    v = 0
    x = 0
    t = 0
    akceleracije = []
    brzine = []
    pomaci = []
    vrijeme = []
    for i in range(20):
        v = v + a*d_t
        x = x + v*d_t
        t += d_t
        brzine.append(v)
        pomaci.append(x)
        vrijeme.append(t)
        akceleracije.append(a)

    plt.subplot(311)
    plt.plot(vrijeme, pomaci)
    plt.title('x-t graf')
    plt.subplot(312)
    plt.plot(vrijeme, brzine, 'r')
    plt.title('v-t graf')
    plt.subplot(313)
    plt.plot(vrijeme, akceleracije, 'g')
    plt.title('a-t graf')
    plt.show()



def kosi_hitac(v0,theta,t):
    theta_1 = radians(theta)
    v_x = v0 * cos(theta_1)
    x = 0
    y = 0
    dt = 0.5
    N = t * 2

   
    t = 0
    g = 9.81
    t_l = []
    x_l = []
    y_l = []


    for i in range(N):
        x = v_x * t
        y = v0*sin(theta_1)*t -0.5*g*t*t
        t += dt

        x_l.append(x)
        y_l.append(y)
        t_l.append(t)

    plt.subplot(311)
    plt.plot(x_l,y_l, 'g')
    plt.subplot(312)
    plt.plot(t_l,x_l)
    plt.subplot(313)
    plt.plot(t_l,y_l, 'r')
    plt.show()
 
kosi_hitac(12,30,10)

import numpy as np
def deriviraj(func,h,x):
    d = (func(h+x)-func(x-h))/(2*h)
    return d 
    
def derivacija(func,h,x1,x2):
    
    d_lista = []
    x_lista = np.arange(x1,x2,h)
    
    for x in x_lista:
        d = deriviraj(func,h,x)
        d_lista.append(d)


    return x_lista,d_lista

def integriraj(func,a,b,N):
    dx = (b-a)/N
    x_g = a
    x_d = a+dx 
    d_l = []
    g_l = []
    g_m = 0
    d_m = 0
    xg_l = []
    xd_l = []
    for i in range(N):
        g_m += func(x_g)*dx
        d_m += func(x_d)*dx
        xg_l.append(x_d)
        xd_l.append(x_g)
        x_d+= dx
        x_g += dx
        g_l.append(g_m)
        d_l.append(d_m)  
    return g_m,d_m
def integracija(func,a,b,N):
    dx = (b-a)/N
    xk = a
    suma = 0
    for i in range(N):
        suma += (func(xk) + func(xk+dx))
        xk += dx
    integ = (dx/2)*suma
    return integ


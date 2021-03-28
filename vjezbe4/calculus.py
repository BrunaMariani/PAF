
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
    x_g = a + dx
    x_d = a
    g_m = 0
    d_m = 0
    for i in range(N):
        g_m += func(x_g)*dx
        d_m += func(x_d)*dx
        x_d+= dx
        x_g += dx
    print(f'Gornja međa je {g_m}, a donja {d_m}')

def integracija(func,a,b,N):
    dx = (b-a)/N
    xk = a
    suma = 0
    for i in range(N):
        suma += (func(xk) + func(xk+dx))
        xk += dx
    integ = (dx/2)*suma
    print(integ)



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



    

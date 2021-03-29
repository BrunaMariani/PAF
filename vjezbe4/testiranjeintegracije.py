import calculus
import matplotlib.pyplot as plt
import modul
import math
import numpy as np

def f1(x):
    return 2*x**2-3


a,b,c,d = calculus.integracija(f1,0,2,100)
plt.plot(a,c)
plt.show()

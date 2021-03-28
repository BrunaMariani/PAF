import calculus
import matplotlib.pyplot as plt
import modul
import math
import numpy as np

def f4(x):
    return 5*x**3 - 2*x**2+2*x-3
calculus.integracija(f4,2,6,100)
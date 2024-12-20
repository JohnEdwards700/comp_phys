from math import *
from scipy.optimize import fsolve, bisect, newton
import numpy as np
import matplotlib.pyplot as plt

x0 = 10 #float(input("Enter a starting value: x0 = "))
tolerance =  0.1#float(input('Enter a Tolerance: '))
N = 100
def f(x):
    return 3*x + 2*x*x -5 - 10*np.cos(x)
    # return x*np.exp(x)/(np.exp(x)-1) -5

def fprime(x):
    return 3 + 4*x + 10*np.sin(x)

x = np.linspace(-10,10,200)
y = f(x)
plt.plot(x, y, 'cD',)
plt.plot(x,np.zeros(200),'r-')

def func(N=100):
    for i in range(N):
        x = x0
        x0 = x - f(x)/fprime(x)
        if abs(x-x0) < tolerance:
            print(f'stop at i = {i}\nRoot is {x0} to within {tolerance}')
            break
        
# func()

print(f'Fsolve: {fsolve(f,-2.0)}')
print(f'Bisect: {bisect(f,-1.0, 5)}')
print(f'Newton: {newton(f, -2.0)}')
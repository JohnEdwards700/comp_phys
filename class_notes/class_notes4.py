import matplotlib.pyplot as plt
import numpy as np 

## Ploting Functions in Python

def f(x):
    return np.cos(x) - np.exp(-x)

# arrange linspace

# x = np.arange(-2, 2, 0.01)
x = np.linspace(-2, 2, 400)

plt.plot(x, f(x), 'g-')
# plt.plot(x, -x*x, '-r')

derivative = np.diff(f(x))/0.01

plt.plot(x[:-1], derivative,'-b')

plt.show()

#### UNFINISHED #####

##Animating Graphs

import matplotlib.animation as animation

fig, ax = plt.subplots()

t = np.linspace(0,3, 50)

#acceleration due to gravity

GRAVITY = 9.8

v01 = 20
v02 = 10

z1 = v01*t - 1/2*GRAVITY*t**2
z2 = v02*t - 1/2*GRAVITY*t**2

# plot 

scat = ax.scatter(t[0], z1[0], c = 'b', label = f'v01 = {v01} m/s')

line2 = ax.plot(t[0], z2[0], c = 'b', label = f'v02 = {v02} m/s')

ax.set(xlim = [0,4], ylim = [-4, 40], xlabel = 'Time [s]', ylabel = 'z [m]')
ax.legend()

def update(frame):
    x = t[:frame]
    y = z1[:frame]
    #update plot
    
    ##### UNFINISHED ######




import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 

#Lorenz system
def lorenz(x,y,z,s=10, r=28, b=2.667):
    x_dot = s*(y-x)
    y_dot = r*x -y - x*z
    z_dot = x * y - b * z 
    
    return x_dot, y_dot, z_dot

#time step
h = 0.01

stepCnt = 10000
xs = np.empty((stepCnt+1,))
ys = np.empty((stepCnt+1,))
zs = np.empty((stepCnt+1,))

# initial values
xs[0],ys[0],zs[0] = (0, 1.0, 1.05)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(xs,ys,zs)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

for i in np.arange(stepCnt):
    #derivative
    x_dot,y_dot,z_dot = lorenz(xs[i],ys[i],zs[i])
    #Euler
    xs[i+1] = xs[i] + x_dot*h
    ys[i+1] = ys[i] + y_dot*h
    zs[i+1] = zs[i] + z_dot*h
    
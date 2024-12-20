import numpy as np 
import matplotlib.pyplot as plt 

#initial params
g = 9.81
v0 = 25 #initial velocity in m/s
vt = 9  #terminal velocity
h = 0.01
v = v0
t = 0
y = 1.5

#create arrays 

tc = np.zeros(1)
yc = np.zeros(1)
tc[0] = 0
yc[0] = 1.5


#defome acceleration function
def a(v):
    return -g*(1+v*abs(v)/vt**2)

def Huen(v):
    vend = v + a(v) *h
    v = v + (a(v) + a(vend))/2*h
    return v
    
def Huen_y(v,y): 
    y_end = y + v*h 
    y = y + (v+v)/2*h  
    return y

while y >= 0:
    v = Huen(v)
    y = Huen_y(v, y)
    yc= np.append(yc,y)
    t = t + h
    tc = np.append(tc,t)
    
maxHeight = yc[np.argmax(yc)]
maxHeightTime = tc[np.argmax(yc)]  

print(f'Max Height = {maxHeight}\n Max Height Time = {maxHeightTime}')
plt.xlabel('Time')
plt.ylabel('Position')
plt.plot(tc,yc,'b-', label='line')
plt.show()


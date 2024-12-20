import numpy as np 
import matplotlib.pyplot as plt 

#initial params
g,v0,vt,theta = 9.81 , 40, 45, 45
h = dt = 0.01

#create arrays 

tc = np.zeros(1)
yc = np.zeros(1)
xc =np.zeros(1)

tc[0] = 0
yc[0] = 1.5
xc[0] = 0

v = v0
x = 0
y=1.5
t=0

vx = v0*np.cos(theta*np.pi/180)
vy = v0*np.sin(theta*np.pi/180)


#defome acceleration function
def ay(vy, v):
    return -g*(1+vy*v/vt**2)

def ax(vx, v):
    return -g*vx*v/vt**2

def Huen_vx(vx,v):
    vend = vx + ax(vx,v) *dt
    vx = v + (ax(vx,v) + ax(vend, v))/2*h
    return vx
    
def Huen_vy(vy,v): 
    y_end = vy + ay(vy,v)*h 
    vy = vy + (ay(vy,v)+ay(y_end,v))/2*h  
    return vy

def Huen(position,velocity):
    return position + velocity*dt

while y >= 0:
    vx = Huen_vx(vx,v)
    x = Huen(x, vx)
    vy = Huen_vy(vy,v)
    y = Huen(y,vy)
    v = np.sqrt(vx**2 + vy**2)
    xc = np.append(xc, x)
    yc= np.append(yc,y)
    t = t + h
    tc = np.append(tc,t)
    
maxHeight = yc[np.argmax(yc)]
maxHeightTime = tc[np.argmax(yc)]  
crange = xc[np.argmax(xc)]
timeOfFlight = tc[np.argmax(xc)]

# print(f'Max Height = {maxHeight}\n Max Height Time = {maxHeightTime}\n Range = {crange}\n Time of Flight = {timeOfFlight}')
plt.xlabel('Time')
plt.ylabel('Position')
plt.plot(xc,yc,'b-', label='line')
plt.show()


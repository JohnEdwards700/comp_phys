import numpy as np 
import matplotlib.pyplot as plt 

#initial params
g,v0,vt = 9.81 , 35, 9
h = dt = 0.01

#create arrays 

xc = np.zeros(0)
thetac = np.zeros(0)

v = v0
x = 0
y=1.5
t=0



#defome acceleration function
def ay(vy, v):
    return -g*(1+vy*v/vt**2)

def ax(vx, v):
    return -g*vx*v/vt**2

def Huen_vx(vx,v):
    vend = vx + ax(vx,v) *dt
    vx = vx + (ax(vx,v) + ax(vend, v))*dt/2
    return vx
    
def Huen_vy(vy,v): 
    y_end = vy + ay(vy,v)*h 
    vy = vy + (ay(vy,v)+ay(y_end,v))*dt/2
    return vy

def Huen(position,velocity):
    return position + velocity*h

def throw(vx,vy,v):
    t = 0
    y=1.5
    x = 0
    while y >= 0:
        vx = Huen_vx(vx,v)
        x = Huen(x, vx)
        vy = Huen_vy(vy,v)
        y = Huen(y,vy)
        v = np.sqrt(vx**2 + vy**2)
        t = t + h
    return x

#Loop over angles adn determine th range for each angle
for theta in np.arange(0, 60, 0.5):
    vx = v0*np.cos(theta*np.pi/180)
    vy = v0*np.sin(theta*np.pi/180)
    v = np.sqrt(vx**2 + vy**2)
    x = throw(vx,vy,theta)
    xc = np.append(xc,x)
    thetac = np.append(thetac,theta)
    
# xc = np.append(xc,x)    
maxHeight = thetac[np.argmax(xc)]
# maxHeightTime = tc[np.argmax(yc)]  
crange = xc[np.argmax(xc)]

# timeOfFlight = tc[np.argmax(xc)]
print(f'Max Range = {crange}')
# print(f'Max Height = {maxHeight}\n Max Height Time = {maxHeightTime}\n Range = {crange}\n Time of Flight = {timeOfFlight}')
plt.xlabel('Angle Theta (degrees)')
plt.ylabel('Horizontal Distance (m)')
plt.plot(thetac,xc,'b-', label='line')
plt.show()


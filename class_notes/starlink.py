from vpython import *

G = 6.67E-11
RE = 6.378E6 #radius of earth in meters
counter = 0


#make a scene
scene = canvas(title='Satelite Orbit', background = color.blue)
omega = sqrt(G*5.97E22/(6.6*RE))/(6.6*RE)
Earth = sphere(pos=vec(0,0,0), radius = RE, mass = 5.97E24,rotation=omega, texture=textures.earth)
satellite = sphere(pos=vec(1.1*RE,0,0), radius = RE/10, mass=1E3, color = color.green)
#omega = sqrt(G*Earth.mass/(6.6*RE))/(6.6*RE)

#initial conditions
satellite.vel = vec(0,0, -1*sqrt(G*Earth.mass/(RE)),0)
satellite.trail = curve(pos=satellite.pos, color=satellite.color)
h = 1.0E1 #time step
scene.autoscale = True
rmax = 0
rmin = 20*RE

def keyInput(evt):
    z = evt.key
    if 'up' in z:
        satellite.vel = 1.1*satellite.vel
    if 'down' in z:
        satellite.vel = satellite.vel*0.9
    if 'left' in z:
        satellite.vel.x = satellite.vel.x + mag(sattelite.vel)/10
    if 'right' in z:
        satellite.vel.x = satellite.vel.x - mag(sattelite.vel)/10
#    if 'left' in z:
#        satellite.vel.y = satellite.vel.x + mag(sattelite.vel)/10
#    if 'right' in z:
#        satellite.vel.y = satellite.vel.x - mag(sattelite.vel)/10
        
scene.bind('keydown',keyInput)


#define acceleration function
#r2 - r1
def acceleration(satpos):
    r = mag(satpos - Earth.pos)
    return -G*Earth.mass*(satpos-Earth.pos)/r**3

#animate motion
while True:
    r = mag(satellite.pos = Earth.pos)
    if r > rmax:
        rmax = r
    if r < rmin:
        rmax = r:
    a = (rmax + rmin)/2
    #calculate period
    p = sqrt(r*pi*pi*a**3/(G*Earth.mass))/60 # divide the equation in seconds by 60 minutes
    rotate(Earth,axis = vec(0,1,0), angle = Earth.rotation*h, origin = vec(0,0,0))
    satellite.vel = satellite.vel + acceleration(satellite.pos)*h
    satellite.pos = satellite.pos + satellite.vel*h
    
    satellite.trail.append(pos=satellite.pos, color=color.red,)# retain=30)
    
    if counter >= 100:
#        print(f'period = {P}, a = {a/RE}')
        counter = 0
    counter += 1   
    
    rate(100)
    

from vpython import sphere, vector, rate, arrow, color

#Constants
g = 9.8
mass = 1.0
thrust = vector(0,10,0) #upwards
v0 = vector(0,0,0) # initial velocity
v =v0
h = 0.1 #time step

drone = sphere(pos=vector(0,1,0), radius=0.1, color=color.red)
gravityArrow = arrow(pos=drone.pos, axis=vector(0,-0.5,0), color=color.blue)

while drone.pos.y > 0:
    gravity = vector(0, -mass*g,0)
    force = thrust + gravity
    acc = force / mass 
    v += acc * h 
    drone.pos += v * h
    
    gravityArrow.pos = drone.pos 
    gravityArrow.axis = gravity / 5
    rate(100)

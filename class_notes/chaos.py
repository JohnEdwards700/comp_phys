import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider, Button, RadioButtons

ax = plt.subplot(111)
plt.subplots_adjust(left=0.25, bottom=0.25)

t = np.arange(0.0, 1.0, 0.01)
tcount = len(t)
#creared array for population
xs = np.zeros(tcount)
#initial values
a0 = 0.5
xs[0] = 0.5
r0 = 0.25/2
r = r0 

#iterate through count and calculte population with predication
for i in range(0,tcount-1):
    xs[i+1] = 4.0*r*xs[i]*(1 - xs[i])
    
l, = plt.plot(t,xs, lw=2, color='red')

plt.axis([0, 1, 0, 1])
plt.xlabel('n')
plt.ylabel('x')
plt.title('Nonlinear Map $x_{n+1} = 4rx_n(1-x_n)$')
#create axes
axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03])
axamp = plt.axes([0.25, 0.15, 0.65, 0.03])
rfreq = Slider(axfreq, 'r', 0.1, 1.0, valinit=r0)
samp = Slider(axamp, 'x0', 0.1, 1.0, valinit=a0)

def update(val):
    amp = samp.val
    r = rfreq.val
    xs[0] = amp
    for i in range(0, tcount-1):
        xs[i+1] = 4.0*r*xs[i]*(1.0-xs[i])
    l.set_ydata(xs)
    plt.draw()
rfreq.on_changed(update)
samp.on_changed(update)
#reset axes on change of r or x
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
def reset(event):
    rfreq.reset()
    samp.reset()
button.on_clicked(reset)
#create radio buttons for color of plot
rax = plt.axes([0.025, 0.5, 0.15, 0.15])
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)
def colorfunc(label):
    l.set_color(label)
    plt.draw()
radio.on_clicked(colorfunc)
plt.show()
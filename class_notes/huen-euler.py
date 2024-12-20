import numpy as np 
import matplotlib.pyplot as plt 

def der_f(y):
    return y**2+1

N=100
x = np.linspace(0,1,N)
h=x[1] -x[0]
y = np.zeros(N)
ym = np.zeros(N)
yh = np.zeros(N)

y[0] = 0

#Euler Algo
for i in range(1,N):
    y[i] = y[i-1] + der_f(y[i-1])*h

#Modified Euler
for i in range(1,N):
    #find midpoint of y(x)
    ymid = ym[i-1] + der_f(ym[i-1])*h/2
    ym[i] = ym[i-1] + der_f(ymid)*h
    
#Heun's method
for i in range(1,N):
    #find end point of interval
    yend = yh[i-1] + der_f(yh[i-1])*h 
    yh[i] = yh[i-1] + (der_f(yh[i-1]) + der_f(yend))/2*h 
    
plt.plot(x,y,'bx',label='Euler')
plt.plot(x,ym, 'co', label='Midpoint')
plt.plot(x,yh,'g^',label='Huen\'s')
plt.plot(x,np.tan(x),'bx',label='Exact')

# plt.plot(x,np.tan(x) - y,'bx',label='Euler')
# plt.plot(x,np.tan(x) - ym, 'co', label='Midpoint')
# plt.plot(x,np.tan(x) - yh,'g^',label='Huen\'s')
# plt.plot(x,0,'bx',label='Exact')

plt.legend()
plt.show()


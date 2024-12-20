import numpy as np 
import matplotlib.pyplot as plt 

##derivative of decay is the time it has been alive

#define functions for rates

def rate1(N1):
    return -k1*N1

def rate2(N1, N2):
    return k1*N1 - k2*N2

def rate3(N2,N3):
    return k2*N2 - k3*N3

k1 = 0.15
k2 = 0.2
k3 = 0.25
nuntime = 200

t = np.linspace(0,30,nuntime)
h = t[1] -t[0]

N1 = np.zeros(nuntime)
N2 = np.zeros(nuntime)
N3 = np.zeros(nuntime)

N1[0] = 100
N2[0] = 0

for i in range(1, nuntime):
    N1[i] = N1[i-1] + rate1(N1[i-1])*h
    N2[i] = N2[i-1] + rate2(N1[i-1], N2[i-1])*h
    N3[i] = N3[i-1] + rate3(N2[i-1], N3[i-1])*h
    
N2_max = max(N2)
t_max_index = np.argmax(N2)
t_max = t[t_max_index]

    
plt.plot(t, N1, 'r-', label='Parent')
plt.plot(t, N2, 'b-', label='Child')
plt.plot(t, N3, 'c-', label='GrandChild')
plt.legen()
plt.show()

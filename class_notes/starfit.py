import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np 

data = np.loadtxt('star_var1.txt', skiprows=0)
x = data[:,0]
y = data[:,1]

def test(x,a,b):
    return a*np.sin(b*x)

param, param_cov = curve_fit(test, x, y)

print("Fitted sine function coefficients")
print(param)
print('Covariance of coefficient')
print(param_cov)



aFit = param[0]
bFit = param[1]
xFit = np.linspace(x[0], x[-1], 100)
yFit = aFit*np.sin(bFit * xFit)
paramError = np.sqrt(np.diag(param_cov))

print(f'Parameter errors = {paramError}')
print(f'Amplitude a = {aFit} +/-  {paramError[0]}, Frequency b = {bFit} +/- {paramError[1]}')

plt.title('Variable star fluctiations')
plt.xlabel('Time [d]')
plt.ylabel('Magnitude')
plt.plot(x,y,'ro', label = 'data')
plt.plot(xFit, yFit, '--', color='blue', label = 'optimized data')
plt.legend()
plt.show()
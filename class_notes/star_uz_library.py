import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np 

data = np.loadtxt('/home/jtedwards/Ubuntu_Code/Projects/comp_phys/text-files/UZLyrO_C_Residuals.txt', skiprows=0)
x = data[:,0]
y = data[:,1]

def test(x,a,b,c,d):
    return a*np.cos(2*np.pi/b*x + c ) + d

A0,B0,C0,D0 = np.std(y), 1600, 0, np.mean(y)
param, param_cov = curve_fit(test, x, y, p0=[A0,B0,C0,D0])

print("Fitted sine function coefficients")
print(param)
print('Covariance of coefficient')
print(param_cov)



aFit = param[0]
bFit = param[1]
cFit = param[2]
dFit = param[3]
xFit = np.linspace(x[0], x[-1], 100)
yFit = aFit*np.cos(2*np.pi/bFit * xFit + cFit) + dFit
paramError = np.sqrt(np.diag(param_cov))
aUncertain = paramError[0]
bUncertain = paramError[1]
cUncertain = paramError[2]
dUncertain = paramError[3]


print(f'Parameter errors = {paramError}')
print(f'Amplitude a = {aFit} +/-  {aUncertain}, Frequency b = {bFit} +/- {bUncertain}, Phase c = {cFit} +/- {cUncertain}, Offset d = {dFit} +/- {dUncertain}')

plt.title('Variable star fluctuations')
plt.xlabel('Time [d]')
plt.ylabel('Residuals [Magnitude]')
plt.plot(x,y,'ro', label = 'data')
plt.plot(xFit, yFit, '--', color='blue', label = 'optimized data')
plt.legend()
plt.show()
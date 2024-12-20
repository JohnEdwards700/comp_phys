import numpy as np 
import matplotlib.pyplot as plt 

# data = np.loadtxt('Afghan1974-2019.txt',str, skiprows=0)
data = np.loadtxt('/home/jtedwards/Ubuntu_Code/Projects/comp_phys/text-files/antarctica_mass_200204_202006.txt',str, skiprows=31)


years = x = np.asfarray(data[:,0])
population = y = np.asfarray(data[:,1])
error = np.asfarray(data[:,2])
N = len(x)

def lstsqr(x,y):
    sumx = 0
    sumy = 0
    sumxx = 0
    sumxy = 0
    A = 0
    B = 0
    
    sumx = sum(x)
    sumy = sum(y)
    sumxx = sum(x*x)
    sumxy = sum(x*y)
    
    Delta = (N*sumxx - sumx*sumx)
    A = (sumxx*sumy - sumx*sumxy)/Delta
    B = (N*sumxy - sumx*sumy)/Delta 
    
    unc_A =  np.sqrt(sum((y - (A+B*x))**2)/(N-2))*np.sqrt(sumxx/Delta)
    unc_B =  np.sqrt(sum((y - (A+B*x))**2)/(N-2))*np.sqrt(N/Delta)  
    
    
    return [A, B, unc_A, unc_B]

def chi_calc(x,y,A,B):
    chi_squared = 0
    sigy = np.std(y)
    for i in range(N):
        chi_squared = chi_squared + (y[i] - (A + B*x[i]))**2/sigy**2
    return chi_squared

def r_calc(x, y):
    r = 0
    sum_diff_xy = 0
    sum_xdiff_square = 0
    sum_ydiff_square = 0
    
    x_bar = np.mean(x)
    y_bar = np.mean(y)
    
    sum_xdiff_square = sum((x- x_bar)**2)
    sum_ydiff_square =  sum((y-y_bar)**2)
    sum_diff_xy = sum((x-x_bar)*(y - y_bar))
    
    r = sum_diff_xy/np.sqrt(sum_xdiff_square*sum_ydiff_square)

    
    return r

coefficients = lstsqr(years,population)

A = coefficients[0]
B = coefficients[1]
unc_A = coefficients[2]
unc_B = coefficients[3]

N_trial = 1000 #number of trial runs
fitPars = np.array([]) #initiilizing array to store A,B, uncertainties from each trial

A_values = np.zeros(N_trial)
B_values = np.zeros(N_trial)
unc_A_values = np.zeros(N_trial)
unc_B_values = np.zeros(N_trial)
y_err =  np.sqrt(sum((y-(A + B * x))**2)/(N-2))
xmin = x[0]
xmax = x[-1]

#create random data
for j in range(N_trial):
    xtrial = np.random.uniform(xmin, xmax, size=N)
    ytrial = A + B*xtrial + np.random.normal(loc=0, scale = y_err, size=N)
    A_values[j], B_values[j], unc_A_values[j], unc_B_values[j] = lstsqr(xtrial, ytrial)
    
#multiaxis hisogram

fig = plt.figure(figsize=(6,6))
fig.suptitle('Monte Carlo Estimaton of Parameters')
grid = plt.GridSpec(4,4,hspace=0.4, wspace=0.5)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1,0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1,1:], yticklabels=[], sharex=main_ax)

#scatter plot on main axes
main_ax.plot(A_values, B_values, 'ok', markersize=2, alpha=0.2)

#create histograms on axes
x_hist.hist(A_values, 50, histtype='stepfilled', orientation='vertical', color = "blue")
y_hist.hist(B_values, 50, histtype='stepfilled', orientation='horizontal', color = "red")

y_hist.invert_xaxis()
plt.show()

A = np.mean(A_values)
B = np.mean(B_values)
unc_A = np.mean(unc_A_values)
unc_B = np.mean(unc_B_values)

print(f'Coefficients: A = {A} +/- {unc_A}, B = {B} +/- {unc_B}')


# print(A, B, chi_calc(x,y,A,B)/(N-2), r_calc(x,y))

# plt.plot(x,y,'bo')

# xc = np.linspace(x[0], x[N-1], 200)
# yc =  A + B*xc
# plt.plot(xc, yc, 'r+')
# plt.title('Churhc and White')
# plt.xlabel("year")
# plt.ylabel('sea level change (mm)')

# plt.errorbar(x,y,yerr=error, ecolor='purple',capsize=2)


# fig, ax = plt.subplots()
# dy = y - (A+B*x)
# ax.plot(x, (A + B*x), 'r-')
# ax.scatter(x,y,c='b')
# ax.vlines(x,y,y-dy,'c')
# plt.legend(('Least Squares Fit', 'Data', 'Residuals'), loc = 0)
# plt.show()
# import numpy as np 
# import matplotlib.pyplot as plt 

# # data = np.loadtxt('Afghan1974-2019.txt',str, skiprows=0)
# # data = np.loadtxt('CSIRO_Recons_gmsl_mo_2011.txt',str, skiprows=0)


# years = x = np.asfarray(data[:,0])
# population = y = np.asfarray(data[:,1])
# N = len(x)

# def lstsqr(x,y):
#     sumx = 0
#     sumy = 0
#     sumxx = 0
#     sumxy = 0
#     A = 0
#     B = 0
    
#     sumx = sum(x)
#     sumy = sum(y)
#     sumxx = sum(x*x)
#     sumxy = sum(x*y)
    
#     Delta = (N*sumxx - sumx*sumx)
#     A = (sumxx*sumy - sumx*sumxy)/Delta
#     B = (N*sumxy - sumx*sumy)/Delta   
    
    
#     return [A, B]

# def chi_calc(x,y,A,B):
#     chi_squared = 0
#     sigy = np.std(y)
#     for i in range(N):
#         chi_squared = chi_squared + (y[i] - (A + B*x[i]))**2/sigy**2
#     return chi_squared

# def r_calc(x, y):
#     r = 0
#     sum_diff_xy = 0
#     sum_xdiff_square = 0
#     sum_ydiff_square = 0
    
#     x_bar = np.mean(x)
#     y_bar = np.mean(y)
    
#     sum_xdiff_square = sum((x- x_bar)**2)
#     sum_ydiff_square =  sum((y-y_bar)**2)
#     sum_diff_xy = sum((x-x_bar)*(y - y_bar))
    
#     r = sum_diff_xy/np.sqrt(sum_xdiff_square*sum_ydiff_square)
    
#     return r

# coefficients = lstsqr(years,population)

# A = coefficients[0]
# B = coefficients[1]

# print(A, B, chi_calc(x,y,A,B)/(N-2), r_calc(x,y))

# plt.plot(x,y,'bo')

# xc = np.linespace(x[0], x[N-1], 200)
# yc =  A + B*xc
# plt.plot(xc, yc, 'r+')
# plt.show()

import numpy as np 
import matplotlib.pyplot as plt 

# data = np.loadtxt('Afghan1974-2019.txt',str, skiprows=0)
data = np.loadtxt('antarctica_mass_200204_202006.txt',str, skiprows=31)


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
    
    
    return [A, B]

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

print(A, B, chi_calc(x,y,A,B)/(N-2), r_calc(x,y))

plt.plot(x,y,'bo')

xc = np.linspace(x[0], x[N-1], 200)
yc =  A + B*xc
plt.plot(xc, yc, 'r+')
plt.title('Churhc and White')
plt.xlabel("year")
plt.ylabel('sea level change (mm)')

plt.errorbar(x,y,yerr=error, ecolor='purple',capsize=2)


fig, ax = plt.subplots()
dy = y - (A+B*x)
ax.plot(x, (A + B*x), 'r-')
ax.scatter(x,y,c='b')
ax.vlines(x,y,y-dy,'c')
plt.legend(('Least Squares Fit', 'Data', 'Residuals'), loc = 0)
plt.show()
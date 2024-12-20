import matplotlib.pyplot as plt 
import numpy as np
import statistics as st

data = np.loadtxt('stars.txt', float, skiprows=1)
    
    
temps = data[:,1]
print(temps)
luminosity = data[:,0]
print(luminosity)

meanLum = st.mean(luminosity)
deviationLum = st.stdev(luminosity)
meanTemp = st.mean(temps)
deviationTemp = st.stdev(temps)

print(f'Answer A: The Magnitude Mean is {meanLum} and Temp mean is {meanTemp} \nThe Standard deviation for Magnitude is {deviationLum} and for Temps is {deviationTemp}\n')

    
# print(temps, "\n" ,luminosity)

numTemps = len(temps)
numLumin = len(luminosity)

fig, axs = plt.subplots(1,3, figsize=(8,6), tight_layout=True)

axs[0].hist(temps, numTemps, color='green')
axs[0].set_title('Temperature vs Number Stars')
axs[0].set_xlabel('Temperature')
axs[0].set_ylabel('Number of Stars')


axs[1].hist(luminosity, numLumin, color='red', edgecolor='blue')
axs[1].set_title('Luminosity vs Number Stars')
axs[1].set_xlabel('Magnitude')
axs[1].set_ylabel('Number of Stars')

axs[2].plot(luminosity, temps, label='Magnitude Vs. Temperature', color='purple')
axs[2].set_title('Magnitude Vs. Temperature')
axs[2].invert_xaxis()
axs[2].invert_yaxis()
axs[2].set_xlabel('Temperature (C)')
axs[2].set_ylabel('Magnitude')



# plt.plot(numLumin, numTemps, label='Historagram', color='red')
plt.show()
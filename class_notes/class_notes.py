import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('sunspots.txt', float, skiprows=1, max_rows=1000)

monthNum = data[:,0]
SunspotNum = data[:,1]
def running_average(data, total_month):
    averages = []
    for i in range(len(data) - total_month + 1):
        month = data[i:i + total_month]
        month_average = sum(month) / total_month
        averages.append(month_average)
    
    return averages

months = 12
running_avg = running_average(SunspotNum, months)

adjusted_monthNum = monthNum[months-1:]

plt.plot(monthNum, SunspotNum, label='Original Data')

plt.plot(adjusted_monthNum, running_avg, label='Running Average', color='red')

plt.xlabel("Time [months]")
plt.ylabel("Sunspots Number")
plt.legend()

plt.savefig("sunspots_with_running_avg.png")
plt.show()

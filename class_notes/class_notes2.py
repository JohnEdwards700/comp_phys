import numpy as np
import matplotlib.pyplot as plt

#calculate integers from 1 to 100
watermelon = 100
def watermelonthings():
    for day in range(0,101):
        w_water = watermelon*0.99
        w_water = w_water - 1
        watermelon = w_water + 1
        percent = w_water/watermelon*100
        
        if percent < 98.0:
            print("Percentage of Water in Water Melon: ", percent)
        else:
            print(day, watermelon, percent)
        
## 9/11/24 Notes ##

##.zfill(int) exapnds your string int three places for example 001 or 238

s =  "1101001011"
m = list(filter(lambda x: x == "1",s))
# print(m)

## End of 9/11/24 Notes ##


## 9/13/24 Notes ##

########################

l = [2, 64, 66, 100]

l[0:4:2]

# l[start:stop:step]

###########################

# data = [28, 48, 71, 2, 77, 90]

# sum = 0 

# x_bar = np.mean(data)

# for i in range(0, len(data)):
#     sum = sum + (data[i] - x_bar)**2
    
# std = np.sqrt(sum/len(data))
# print(std)

# print(np.std(data))

##########################

data = np.loadtxt('sunspots.txt', float, skiprows=1)

#slicing data to find month and num into two arrays
monthNum = data[:,0]

SunspotNum = data[:,1]

#number of entries --- datapoints


n = len(monthNum)

plt.plot(monthNum, SunspotNum)
plt.xlabel("Time[months]")
plt.ylabel("Sunspots Number")
plt.savefig("sunspots.png")
plt.show()


## End of NOtes 9/13 ##

    
    
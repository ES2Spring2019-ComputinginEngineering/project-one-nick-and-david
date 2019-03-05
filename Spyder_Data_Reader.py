#
#Contributers: David Fricke and Nicolas Ragusa
#


import math
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt


time_list = []                                     
theta_list = []
angular_acc_list = []

g = -1000                                                    #Microbit gravity constant
a = 2                                                       #Fill to find file number
fin = open('real_pendulum_data' + str(a) + '.txt')

for line in fin:
    a = line.strip()                                  #unpacks data from file
    c = a.split(',')
    time, y = c
    time_list.append(int(time)/1000)                #time into seconds
    angular_acc_list.append(int(y))
    theta = np.arcsin(int(y)/g)                        #Find theta by using gravity and y-acc
    theta_list.append(theta*(180/(math.pi)))
    
# Apply median filter to both original and noisy wave
angular_acc_list_filt = sig.medfilt(angular_acc_list,kernel_size=11)
theta_list_filt = sig.medfilt(theta_list,kernel_size=11)

# Find peaks of all waves 
filt_acc_pks, _ = sig.find_peaks(angular_acc_list_filt)
noisy_acc_pks, _ = sig.find_peaks(angular_acc_list)
filt_theta_pks, _ = sig.find_peaks(theta_list_filt,height=3.75)
noisy_theta_pks, _ = sig.find_peaks(theta_list)

time_of_pks = []
theta_pks = []
x=0

for i in range(len(filt_theta_pks)):
    z = filt_theta_pks[x]
    theta_pks.append(theta_list_filt[z])
    b = time_list[z]
    time_of_pks.append(b)
    x = x + 1
    
    
new_period = []
avg_period = []
average = 0

i = 1
while i < len(time_of_pks):
    if abs(time_of_pks[i-1] - time_of_pks[i]) > .75:
        new_period.append(time_of_pks[i])
    i = i + 1
    
n = 1
while n < len(new_period):
    x = abs(new_period[n-1] - new_period[n])
    avg_period.append(x)
    n = n + 1

for item in avg_period:
    average += item

print('Average period:',round(average/len(avg_period),2),'sec')

plt.figure(figsize=(8,10))

plt.subplot(4,1,1)
plt.plot(time_list, theta_list, 'ro--')
plt.xlabel('Time (seconds)')
plt.ylabel('Theta (Degrees)')
plt.title('Original Theta vs Time')
plt.xlim((0, 14))
plt.grid()

plt.subplot(4,1,2)
plt.plot(time_list, theta_list_filt, 'ro--', time_of_pks, theta_pks, 'b.') 
plt.xlabel('Time (seconds)')
plt.ylabel('Theta (Degrees)')
plt.title('Median Filtered Theta vs Time')
plt.xlim((0, 14))
plt.grid()

plt.subplot(4,1,3)
plt.plot(time_list, angular_acc_list, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acc (Degrees/s^2)')
plt.title('Angular vs Time')
plt.xlim((0, 14))
plt.grid()

plt.subplot(4,1,4)
plt.plot(time_list, angular_acc_list_filt, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acc (Degrees/s^2)')
plt.title('Median Filtered Angular Acceleration vs Time')
plt.xlim((0, 14))
plt.grid()

plt.tight_layout()
plt.show()

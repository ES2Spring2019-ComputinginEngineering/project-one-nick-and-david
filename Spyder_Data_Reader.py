#Real-World Data Analysis
#Contributers: David Fricke and Nicolas Ragusa
#Takes real world pendulum data and provides a original and filtered graph of both theta vs time and angular acceleration vs time
#and provides the average period of oscillation


import math
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt


time_list = []                                     
theta_list = []
angular_acc_list = []

g = -981                                                    #Microbit gravity constant
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

for i in range(len(filt_theta_pks)):           #makes x and y values to plot the location of peaks later after filtering
    z = filt_theta_pks[x]
    theta_pks.append(theta_list_filt[z])
    b = time_list[z]
    time_of_pks.append(b)
    x = x + 1
    
    
period = []
avg_period = []
average = 0

i = 1
while i < len(time_of_pks):                             #filters out peaks that are too close (identifying the same peak)
    if abs(time_of_pks[i-1] - time_of_pks[i]) > .75:
        period.append(time_of_pks[i])
    i = i + 1
    
n = 1
while n < len(period):                              #finds time between neighboring peaks
    x = abs(period[n-1] - period[n])
    avg_period.append(x)
    n = n + 1

for item in avg_period:
    average += item

print('Average period:',round(average/len(avg_period),2),'sec')     #prints a calculated average of period

plt.figure(figsize=(8,10))

plt.subplot(4,1,1)                              #plots theta vs time
plt.plot(time_list, theta_list, 'ro--')
plt.xlabel('Time (seconds)')
plt.ylabel('Theta (Degrees)')
plt.title('Original Theta vs Time')
plt.xlim((0, 14))
plt.grid()

plt.subplot(4,1,2)                              #plots filtered thetas vs time and peaks
plt.plot(time_list, theta_list_filt, 'ro--', time_of_pks, theta_pks, 'b.') 
plt.xlabel('Time (seconds)')
plt.ylabel('Theta (Degrees)')
plt.title('Median Filtered Theta vs Time')
plt.xlim((0, 14))
plt.grid()

plt.subplot(4,1,3)                               #plots angular acceleration vs time
plt.plot(time_list, angular_acc_list, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acc (Degrees/s^2)')
plt.title('Angular vs Time')
plt.xlim((0, 14))
plt.grid()

plt.subplot(4,1,4)                                #plots filtered angular acceleration vs time
plt.plot(time_list, angular_acc_list_filt, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acc (Degrees/s^2)')
plt.title('Median Filtered Angular Acceleration vs Time')
plt.xlim((0, 14))
plt.grid()

plt.tight_layout()
plt.show()

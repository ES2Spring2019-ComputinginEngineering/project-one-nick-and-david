#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:32:14 2019

@author: DRFricke
"""
import math
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt


time_list = []                                      #Fat cut
theta_list = []
angular_acc_list = []


g = -1000                                                    #Microbit gravity constant
a = 9                                                       #Fill to find file number
fin = open('real_pendulum_data' + str(a) + '.txt')

for line in fin:
    a = line.strip()
    c = a.split(',')
    time, y = c
    time_list.append(int(time)/1000)                #time into seconds
    angular_acc_list.append(int(y))
    theta = np.arcsin(int(y)/g)                        #Find theta by using gravity and y-acc
    theta_list.append(theta*(180/(math.pi)))
    
# Apply median filter to both original and noisy wave
angular_acc_list_filt = sig.medfilt(angular_acc_list)
theta_list_filt = sig.medfilt(theta_list)

# Find peaks of all waves (started)
filt_acc_pks, _ = sig.find_peaks(angular_acc_list_filt)
noisy_acc_pks, _ = sig.find_peaks(angular_acc_list)
filt_theta_pks, _ = sig.find_peaks(theta_list_filt)
noisy_theta_pks, _ = sig.find_peaks(theta_list)

time_of_pks = []
theta_pks = []
x=0

for i in range(len(noisy_theta_pks)):
    z = noisy_theta_pks[x]
    theta_pks.append(z)
    b = time_list[z]
    time_of_pks.append(b)
    x = x + 1
    

# for plotter in MU
#x = 0
#for item in angular_acc_list:
#    print((angular_acc_list[x]/100, theta_list[x],))
#    x = x + 1

plt.figure(figsize=(8,10))

plt.subplot(4,1,1)
plt.plot(time_list, theta_list, 'ro--') #, noisy_theta_pks, 'b.'
plt.xlabel('Time (seconds)')
plt.ylabel('Theta (rads)')
plt.title('Original Theta vs Time')
plt.xlim((0, 14))
plt.grid()

plt.subplot(4,1,2)
plt.plot(time_list, theta_list_filt, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Theta (rads)')
plt.title('Median Filtered Theta vs Time')
plt.xlim((0, 14))
plt.grid()

plt.subplot(4,1,3)
plt.plot(time_list, angular_acc_list, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acceleration (rads/s^2)')
plt.title('Angular vs Time')
plt.xlim((0, 14))
plt.grid()

plt.subplot(4,1,4)
plt.plot(time_list, angular_acc_list_filt, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acceleration (rads/s^2)')
plt.title('Median Filtered Angular Acceleration vs Time')
plt.xlim((0, 14))
plt.grid()

plt.tight_layout()
plt.show()

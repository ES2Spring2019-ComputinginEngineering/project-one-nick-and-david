#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:32:14 2019

@author: DRFricke
"""
import math
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
    theta = math.asin(int(y)/g)                        #Find theta by using gravity and y-acc
    theta_list.append(theta*(180/(math.pi)))

# for plotter in MU
#x = 0
#for item in angular_acc_list:
#    print((angular_acc_list[x]/100, theta_list[x],))
#    x = x + 1

plt.figure(figsize=(8,10))
plt.subplot(3,1,1)
plt.plot(time_list, theta_list, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Theta (rads)')
plt.title('Theta vs Time')
plt.xlim((0, 10)) # set x range to -1 to 8
plt.grid()


plt.subplot(3,1,2)
plt.plot(time_list, angular_acc_list, 'ro--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acceleration (rads/s^2)')
plt.title('Angular vs Time')
plt.xlim((0, 10)) # set x range to -1 to 8
plt.grid()
plt.tight_layout()
plt.show()

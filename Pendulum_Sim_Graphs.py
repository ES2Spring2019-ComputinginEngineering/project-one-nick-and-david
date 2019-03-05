#Simulated pendulum data collection and analysis
#Contributers: David Fricke and Nicolas Ragusa
#This code takes manually inputted pendulum lengths and simulates a pendulum of this length running
#and provides graphs of theta vs time, angular velocity vs time, and angular acceleration vs time
#as well as providing the period of oscillation

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.signal as sig

def update_system(acc,theta,w,time1,time2):     #position, velocity, and acceleration update below based on previous time step's data
    dt = time2-time1
    accNext = -9.8/l*(math.sin((theta)))-friction*w
    wNext = w+acc*dt
    thetaNext = theta+w*dt
    return thetaNext,wNext,accNext


# initial conditions
l = 0.447
theta = [.09]
w = [0]
acc = [-9.8/l*(math.sin(theta[0]))]
time = np.linspace(0,14,15000)
#print_system(time[0],theta[0],w[0])
friction = .1


i = 1
while i < len(time):        # update position, velocity, and acceleration using previous values and time step
    thetaNext, wNext, accNext = update_system(acc[i-1], theta[i-1],w[i-1],time[i-1],time[i])
    theta.append(thetaNext)
    w.append(wNext)
    acc.append(accNext)
    #print_system(time[i],theta[i],w[i])
    i += 1
    
short_theta = np.array(theta[::20])
short_time = time[::20]   
# Find peaks of all waves (started)
theta_pks, _ = sig.find_peaks(short_theta)
acc_pks, _ = sig.find_peaks(acc)

time_of_pks = short_time[theta_pks]
short_theta_pks = short_theta[theta_pks]

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
    
print('Average period:',round(average/len(time_of_pks),2),'sec')    #prints the average period of oscillation

plt.figure(figsize=(8,10))              #plots theta vs time, with peaks denoted in blue
plt.subplot(3,1,1)
plt.plot(short_time, short_theta, 'r-', time_of_pks, short_theta_pks, 'b.')
plt.xlabel('Time (seconds)')
plt.ylabel('Theta (rads)')
plt.title('Theta vs Time')
plt.xlim((0, 14))
plt.grid()


plt.subplot(3,1,2)                  #plots angular velocity vs time
plt.plot(time, w, 'ro-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Velocity (rads/s)')
plt.title('Angular Velocity vs Time')
plt.xlim((0, 14))
plt.grid()


plt.subplot(3,1,3)                  #plots angular acceleration vs time
plt.plot(time, acc, 'ro-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acceleration (rads/s^2)')
plt.title('Angular vs Time')
plt.xlim((0, 14)) # set x range to -1 to 8
plt.grid()
plt.tight_layout()
plt.show()

import numpy as np
import math

def update_system(acc,theta,w,time1,time2):
    # position and velocity update below
    dt = time2-time1
    thetaNext = theta+w*dt+1/2*acc*dt
    wNext = w+acc*dt
    return thetaNext,wNext

def print_system(time,theta,w):
    print("TIME:     ", time)
    print("Theta: ", theta)
    print("Angular Velocity: ", w, "\n")

# initial conditions
theta = [0]
w = [0]
acc = 9.8*(math.cos((math.pi/2)-theta[-1]))
time = np.linspace(0,20,21)
print_system(time[0],theta[0],w[0])

i = 1
while i < len(time):
    # update position and velocity using previous values and time step
    thetaNext, wNext = update_system(acc,theta[i-1],w[i-1],time[i-1],time[i])
    theta.append(thetaNext)
    w.append(wNext)
    print_system(time[i],theta[i],w[i])
    i += 1
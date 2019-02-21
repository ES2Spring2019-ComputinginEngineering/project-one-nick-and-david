import numpy as np
import math

def update_system(acc,theta,w,time1,time2):
    # position and velocity update below
    dt = time2-time1
    accNext = -9.8/l*(math.sin((theta)))-friction*w
    wNext = w+acc*dt
    thetaNext = theta+w*dt
    return thetaNext,wNext,accNext

def print_system(time,theta,w):
    print("TIME:     ", time)
    print("Theta: ", theta)
    print("Angular Velocity: ", w, "\n")
    print((theta, w))


# initial conditions
l = 1
theta = [.2]
w = [0]
acc = [-9.8/l*(math.sin(theta[0]))]
time = np.linspace(0,20,50000)
print_system(time[0],theta[0],w[0])
friction = .1


i = 1
while i < len(time):
    # update position and velocity using previous values and time step
    thetaNext, wNext, accNext = update_system(acc[i-1], theta[i-1],w[i-1],time[i-1],time[i])
    theta.append(thetaNext)
    w.append(wNext)
    acc.append(accNext)
    print_system(time[i],theta[i],w[i])
    i += 1

import numpy as np
import math

def update_system(acc,theta,w,time1,time2):
    # position and velocity update below
    dt = time2-time1
    thetaNext = theta+w*dt
    wNext = w+acc*dt
    return thetaNext,wNext

def print_system(time,theta,w):
    print("TIME:     ", time)
    print("Theta: ", theta)
    print("Angular Velocity: ", w, "\n")
    print((theta, w))


# initial conditions
theta = [-.1745]
w = [0]
acc = 9.8*(math.sin((theta[0])))
time = np.linspace(0,30,210)
print_system(time[0],theta[0],w[0])


i = 1
while i < len(time):
    # update position and velocity using previous values and time step
    acc = (-1)*9.8*(math.sin((theta[i-1])))
    print(acc)
    thetaNext, wNext = update_system(acc, theta[i-1],w[i-1],time[i-1],time[i])
    theta.append(thetaNext)
    w.append(wNext)
    print_system(time[i],theta[i],w[i])
    i += 1
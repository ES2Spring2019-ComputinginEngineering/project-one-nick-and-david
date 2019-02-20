import numpy as np
import math

def update_system(acc,pos,vel,time1,time2):
    # position and velocity update below
    dt = time1
    posNext = 10*(math.sin(((acc/.4)**(1/2))*(dt)))
    velNext = 10*((acc/.4)**(1/2))*(math.cos(((acc/.4)**(1/2))*(dt)))
    return posNext,velNext

def print_system(time,pos,vel):
    #print("TIME:     ", time)
    #print("POSITION: ", pos)
    #print("VELOCITY: ", vel, "\n")
    print((pos, vel))

# initial conditions
pos = [0]
vel = [0]
acc = 9.8
time = np.linspace(0,20,200)
print_system(time[0],pos[0],vel[0])

i = 1
while i < len(time):
    # update position and velocity using previous values and time step
    posNext, velNext = update_system(acc,pos[i-1],vel[i-1],time[i-1],time[i])
    pos.append(posNext)
    vel.append(velNext)
    print_system(time[i],pos[i],vel[i])
    i += 1

#Assume length is 0.4 meters
#Assume max theta is 10 degrees
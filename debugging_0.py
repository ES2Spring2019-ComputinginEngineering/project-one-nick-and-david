#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:41:38 2019

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
    print(time)
    time_list.append(int(time)/1000)                #time into seconds
    angular_acc_list.append(int(y))
    theta_list.append(np.arcsin(int(y)/g)*(180/(math.pi)))


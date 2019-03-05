#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:55:54 2019

@author: DRFricke
"""
#Pendulum data analysis code
#Contributers: David Fricke and Nicolas Ragusa
#This code takes manually inputted pendulum lengths and periods (from simulated and real-world data)
#and provides a graph comparing the two

import matplotlib.pyplot as plt

length = [0.447, 0.413, 0.346, 0.298, 0.225]          #manually inputted data (can be changed)
period_actual = [1.26, 1.2, 1.07, 0.99, 0.85]
period_sim = [1.34, 1.29, 1.18, 1.10, 0.95]

plt.figure(figsize=(5,5))                             #sets up graph to display manually inputted data
plt.subplot(1,1,1)
plt.plot(length, period_actual, 'bs', length, period_sim, 'r^')
plt.annotate('Triangle = Simulated Data', xy=(0.27, 1.28))
plt.annotate('Square = Actual Data', xy=(0.27, 1.26))
plt.xlabel('Length (meters)') 
plt.ylabel('Average Period (seconds)')
plt.title('Period vs Length')
plt.xlim((.22, .48))
plt.grid()

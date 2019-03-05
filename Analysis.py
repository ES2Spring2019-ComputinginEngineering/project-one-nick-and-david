#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:55:54 2019

@author: DRFricke
"""
import matplotlib.pyplot as plt

length = [0.447, 0.413, 0.346, 0.298, 0.225]
period_actual = [1.26, 1.2, 1.07, 0.99, 0.85]
period_sim = [1.07, 1.03, 0.97, 0.91, 0.82]

plt.figure(figsize=(5,5))

plt.subplot(1,1,1)
plt.plot(length, period_actual, 'bs', length, period_sim, 'r^')
plt.annotate('Triangle = Simulated Data', xy=(0.27, 1.2))
plt.annotate('Square = Actual Data', xy=(0.27, 1.18))
plt.xlabel('Length (meters)') 
plt.ylabel('Average Period (seconds)')
plt.title('Period vs Length')
plt.xlim((.22, .48))
plt.grid()
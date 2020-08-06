# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:40:57 2020

@author: Silvia Vargas
"""
# import libraries

from main_Brownian_motion import X,Y
import matplotlib.pyplot as plt

# plot the 2D brownian motion
plt.figure(figsize=(15, 7))
plt.title('2D Brownian Motion', fontsize=24)
plt.xlabel('X', fontsize=22)
plt.ylabel('Y', fontsize=22)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)


plt.grid(True, which='major', linestyle='--', color='black', alpha=0.8)
plt.step(X, Y, where='mid')
plt.plot(X[0], Y[0], 'ro')
plt.plot(X[-1], Y[-1], 'go')
plt.show()


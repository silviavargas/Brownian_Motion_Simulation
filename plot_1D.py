# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:26:33 2020

@author: Silvia Vargas
"""
# import libraries

from main_Brownian_motion import X,t
import matplotlib.pyplot as plt

# plot the brownian motion
plt.figure(figsize=(15, 7))
plt.title('Brownian Motion', fontsize=24)
plt.xlabel('Time', fontsize=22)
plt.ylabel('Value', fontsize=22)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.grid(True, which='major', linestyle='--', color='black', alpha=0.8)
plt.step(t, X, where='mid')
plt.plot(t, X, 'C0o', alpha=0.5)
plt.show()




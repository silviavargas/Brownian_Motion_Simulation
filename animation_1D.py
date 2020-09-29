# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 07:59:27 2020

@author: Silvia Vargas
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from Brownian_motion import brownian_motion

fig = plt.figure(figsize=(10, 7))
ax = plt.axes(xlim=(0, 1)) 
line, = ax.step([], [], where='mid', color='#0492C2')
    
# formatting options
ax.set_xticks(np.linspace(0,1,11))
ax.set_xlabel('Time', fontsize=30)
ax.set_ylabel('X', fontsize=30)
ax.tick_params(labelsize=22)
ax.grid(True, which='major', linestyle='--', color='black', alpha=0.6)

# initialization function 
def init():
    line.set_data([], [])
    return line,

# animation function 
def animate(i):
    np.random.seed(42)
    y, dy = brownian_motion((i + 1) * 10, 1 ,1)
    tr = np.linspace(0.0, 1, (i + 1) * 10 + 1)
    ax.set_title('Brownian Motion for {} steps'.format((i + 1) * 10), fontsize=40)
    ax.set_ylim((np.min(y) - 0.1, np.max(y) + 0.1))
    
    line.set_data(list(tr), list(y)) 
    return line,

# call the animator	 
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=150, blit=True)
anim.save('brownian_motion.gif', writer='Pillow')
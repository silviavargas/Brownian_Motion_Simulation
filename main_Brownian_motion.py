# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:13:19 2020

@author: Silvia Vargas 
"""
from Brownian_motion import brownian_motion
import numpy as np


#main part of the code

N = 100 # the number of discrete steps 
T = 1 # the number of continuous time steps
h = 1 # the variance of the increments
dt = 1.0 * T/N # total number of time steps



# generate a brownian motion
Y,dY = brownian_motion(N, T ,h)
X,dX = brownian_motion(N, T ,h)
t = np.linspace(0.0, N*dt, N+1)





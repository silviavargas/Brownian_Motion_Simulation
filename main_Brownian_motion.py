# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:13:19 2020

@author: Silvia Vargas 
"""
import brownian_motion
import numpy as np
import sys
import configparser

#main part of the code
config = configparser.ConfigParser()
config.read(sys.argv[1])

N = config.get('parameter', 'N')
T= config.get('parameter', 'T')
h = config.get('parameter', 'h')
dt = config.get('parameter', 'dt')

destination1 = config.get('paths','my_time')
destination2 = config.get('paths','my_motion')


N = int(N)
T = int(T)
h = float (h)
dt = float(dt)



# generate a brownian motion
X, dX = brownian_motion(N, T ,h)
t = np.linspace(0.0, N*dt, N+1)

np.save(destination1,t)
np.save(destination2,X)

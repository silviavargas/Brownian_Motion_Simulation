# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:54:32 2020

@author: Silvia Vargas
"""
# import libraries
import numpy as np

# set a random seed
np.random.seed(110)


def brownian_motion(N, T, h):
    """
    Generate an instance of Brownian motion (i.e. the Wiener process):

        X(t+dt) = X(t) + N(0,h;t+dt)

    where N(a,b; t0, t1) is a normally distributed random variable with mean a and
    variance b.  The parameters t0 and t1 make explicit the statistical
    independence of N on different time intervals; that is, if [t0, t1] and
    [t2, t3] are disjoint intervals, then N(a, b; t0, t1) and N(a, b; t2, t3)
    are independent.
    
    Arguments
    ---------
    int N : the number of discrete steps
    int T: the number of continuous time steps
    float h: the variance of the increments
    
    Returns
    -------
    Two numpy arrays of floats the random variable X and the increments dX.
    
    Note that the initial value `x0` is not included in the returned array.
    """
    # the normalizing constant
    dt = 1.0 * T/N
    # the random increments values
    dX = np.random.normal(0.0, 1.0 * h, N)*np.sqrt(dt)
    # calculate the brownian motion
    X = np.cumsum(dX)
    # insert the initial condition
    X = np.insert(X, 0, 0.0)
    
    return X, dX

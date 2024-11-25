#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Fri Mar 29 18:07:39 2019

@author: pedro brodude
Modified:  Fri Mar 29 18:07:39 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt

# solve_ode.py

""" ODE solver for harmonic oscillator. """


#import numpy as np, matplotlib.pyplot as plt
from scipy.integrate import odeint


# import ODE to integrate:
from simple_oscillator import F

# Create array of time values to study:
t_min = 0;  t_max=10;  dt =  0.1
t = np.arange(t_min, t_max+dt, dt)


# Provide two sets of initial conditions:
initial_conditions = [ (1,0, 0.0), (0.0, 1.0) ]


plt.figure()     # Create figure; add plots later.

for y0 in initial_conditions:

      y = odeint(F, y0, t)

      plt.plot(t, y[:,0], linewidth=2)


skip = 5

t_test = t[::skip]                                         # compare at a subset of points

plt.plot(t_test, np.cos(t_test), 'bo')        # Exact solution for y0 = (1,0)

plt.plot(t_test, np.sin(t_test), 'go')           # Exact solution for y0 = (0,1)
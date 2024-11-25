#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Mon Apr 15 20:07:30 2019

@author: pedro brodude
Modified:  Mon Apr 15 20:07:30 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt




data = np.loadtxt('PMLSdata/17stressFibers/stressFibers.csv',delimiter=',')

plt.imshow(data)


v = np.arange(-25,26)
X, Y = np.meshgrid(v, v)
gauss_filter = np.exp(-0.5*(X**2/2+Y**2/45))



laplace_filter = np.array(  [      [0,-1,0],   [-1,4,-1],   [0,-1,0]])
combined_filter = sim.convolve(gauss_filter, laplace_filter)

laplace_convolved = sim.convolve(data, laplace_filter)
combined_convolved = sim.convolve(data, combined_filter)


plt.figure()
plt.imshow(data,cmap='gray',vmin=0, vmax=0.5*data.max())

plt.figure()
plt.imshow(laplace_convolved,vmin=0, vmax=0.5*laplace_convolved.max())

plt.figure()
plt.imshow(combined_convolved,vmin=0, vmax=0.5*combined_convolved.max())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Tue Apr 16 13:29:05 2019

@author: pedro brodude
Modified:  Tue Apr 16 13:29:05 2019
Description
____________________

"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sim


photo = plt.imread('bwCat.tif')

#impulse = np.zeros( (51, 51) )

#impulse[25, 25] = 1.0

my_filter = np.ones( (20,20) )/(20**2)

response = sim.convolve(photo, my_filter)


#response  = sim.uniform_filter(photo)

plt.figure()
plt.imshow(response,cmap='gray')
plt.figure()
plt.imshow(photo,cmap='gray')
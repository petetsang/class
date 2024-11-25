#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Mon Apr 15 18:05:38 2019

@author: pedro brodude
Modified:  Mon Apr 15 18:05:38 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sim


photo = plt.imread('bwCat.tif')

#impulse = np.zeros( (51, 51) )

#impulse[25, 25] = 1.0

my_filter = np.ones( (15,15) )/225


response = sim.convolve(photo, my_filter)



#response = sim.uniform_filter(photo)

plt.figure()
plt.imshow(response,cmap='gray')
plt.figure()
plt.imshow(photo,cmap='gray')

















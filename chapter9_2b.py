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
from numpy.random import random as rng




def draw(image):
    plt.imshow(image)
    plt.gray()
    plt.axis('off')


photo = plt.imread('bwCat.tif')



noisy = photo * rng(photo.shape)
noisy -= noisy.min()             # shift min value to zero
noisy *= 255/noisy.max()         # rescale so max is 255
noisy = noisy.astype('uint8')    # convert to standard image array


plt.figure(figsize=(16,8))
plt.subplot(1,2,1)
plt.title("original", fontsize=24, weight='bold')
draw(photo)
plt.subplot(1,2,2)
plt.title("Noisy",fontsize=24,weight='bold')
draw(noisy)



#%% denoise using small, large, gauss
small_square = sim.uniform_filter(noisy, size=3, mode='constant')
large_square = sim.uniform_filter(noisy, size=15, mode='constant')
gauss_dnoise = sim.gaussian_filter(noisy, sigma=5, mode='constant')


plt.figure(figsize=(12,12))
plt.subplot(2,2,1)
plt.title("Noisy", fontsize=24, weight='bold')
draw(noisy)
plt.subplot(2,2,2)
plt.title("Small square", fontsize=24, weight='bold')
draw(small_square)
plt.subplot(2,2,3)
plt.title("Large square", fontsize=24, weight='bold')
draw(large_square)
plt.subplot(2,2,4)
plt.title("Gaussian", fontsize=24, weight='bold')
draw(gauss_dnoise)
plt.savefig('denoising.pdf')


















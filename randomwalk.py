#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Fri Mar  8 19:05:19 2019

@author: pedro brodude
Modified:  Fri Mar  8 19:05:19 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt

from numpy.random import random as rng

def get_trajectory(num_steps):

    
#    walk=[rng(num_steps),rng(num_steps)]
    # random_x contains 500 random numbers from [0 to 1)

    random_x = rng(num_steps)

    random_y = rng(num_steps)

    # random numbers checked for less than 0.5 into a binary true/false

    true_false_x = (random_x < 0.5)

    true_false_y = (random_y < 0.5)

    # binary true_false , (0 or 1) multiplied by 2 into (0, 2) then subtracts 1 into (-1, 1)

    x_step = (true_false_x*2)-1

    y_step = (true_false_y*2)-1

    x_position = np.cumsum(x_step)

    y_position = np.cumsum(y_step)
    
    positions= np.stack([x_position,y_position], axis=1)
    
    return positions
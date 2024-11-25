#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Fri Mar  8 17:33:20 2019

@author: pedro brodude
Modified:  Fri Mar  8 17:33:20 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt

# rotate.py

def rotate_vector(vector, angle):

      """

      Rotate a 2D vector through a given angle.

            vector = (x,y)

            angle = rotate angle in radians (counterclockwise)

      Returns the image of a vector under rotation as a NumPy array.

      """

      rotation_matrix = np.array([[ np.cos(angle),  -np.sin(angle)   ]   ,

                                                   [  np.sin(angle),   np.cos(angle)  ]])

      return np.dot(rotation_matrix, vector)
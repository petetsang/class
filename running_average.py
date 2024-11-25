#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Thu Mar 21 13:17:03 2019

@author: pedro brodude
Modified:  Thu Mar 21 13:17:03 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt

def running_average(x):

      """

      Return cumulative average of an array.

      """

      y = np.zeros(len(x))

      current_sum = 0.0

      for i in range(len(x)):

            current_sum += x[i]

            y[i] = current_sum / (i + 1.0)

      return y
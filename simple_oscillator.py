#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Fri Mar 29 18:01:58 2019

@author: pedro brodude
Modified:  Fri Mar 29 18:01:58 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt


# simple_oscillator.py

def F(y,t):

      """

      Return derivatives for second-order ODE y'' = -y

      """

      dy = [0,0]        # create a list to store derivatives

      dy[0] = y[1]      # Store first derivative of y(t)

      dy[1] = -y[0]     # Store second derivative of y(t)

      return dy
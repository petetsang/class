#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Fri Mar 29 18:02:55 2019

@author: pedro brodude
Modified:  Fri Mar 29 18:02:55 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt

# parametric_oscillator.py

def F(y,t, spring_constant=1.0, mass=1.0):

      """

      Return derivatives for harmonic oscillator:

            y'' = -(k/m) * y

      y = displacement in [m]

      k = spring_constant in [N/m]

      m = mass in [kg]

      """


      dy = [0,0]    # array to store derivatives

      dy[0] = y[1]

      dy[1] = -(spring_constant / mass) * y[0]

      return dy
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Tue Mar 19 13:22:44 2019

@author: pedro brodude
Modified:  Tue Mar 19 13:22:44 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt

# excerpt from measurements.py

def taxicab(pointA, pointB):

       """

       Taxicab metric for computing distance between points A and B.

                  pointA = (x1, y1)

                  pointB = (x2, y2)

       Returns |x2-x1| + |y2-y1|. Distances are measured in city blocks.

       """

       interval = abs( pointB[0] - pointA[0] )   +  abs( pointB[1] - pointA[1] )

       return interval
   
    


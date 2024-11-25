#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Fri Mar  8 17:05:18 2019

@author: pedro brodude
Modified:  Fri Mar  8 17:05:18 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt

# measurements.py

def distance(pointA, pointB=(0,0), metric='taxi'):

      """

      Return distance in city blocks between points A and B.

      If metric is 'taxi' (or omitted), use taxicab metric.

      Otherwise, use Euclidean distance.

             pointA = (x1, y1)

             pointB = (x2, y2)

      If pointB is omitted, use the origin

      """

      if metric == 'taxi':

            interval = abs(pointB[0] - pointA[0]) + abs(pointB[1] - pointA[1])

      else:  

            interval = np.sqrt(   (pointB[0] - pointA[0])**2 \

                                              + (pointB[1] - pointA[1])**2  )

      return interval
  
    
    

def taxicab(pointA, pointB):

       """

       Taxicab metric for computing distance between points A and B.

                  pointA = (x1, y1)

                  pointB = (x2, y2)

       Returns |x2-x1| + |y2-y1|. Distances are measured in city blocks.

       """

       interval = abs( pointB[0] - pointA[0] )   +  abs( pointB[1] - pointA[1] )

       return interval
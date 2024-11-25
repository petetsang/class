#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Sun Apr  7 17:41:20 2019

@author: pedro brodude
Modified:  Sun Apr  7 17:41:20 2019
Description
____________________

"""

# walker.py

# jesse m kinder 2017

""" make a movie out of the steps of a two-dimensional random walk . """

import numpy as np, matplotlib.pyplot as plt

from matplotlib import animation

from numpy.random import random as rand


# set number of steps for each random walk

num_steps = 100


# create an empty figure of the desired size

plt.close('all')

bound = 20

fig = plt.figure()      # you need figure object for a movie   (line 14)

ax = plt.axes(xlim=(-bound, bound), ylim=(-bound, bound)) # (line 15)


# create empty line and point objects with no data. 

# they will be updated during each frame of the animation

(my_line,) = ax.plot([],   [],  lw=2)                 # line to show path

(my_point,) = ax.plot([], [], 'ro', ms=9)       # dot to show current position


# generate the random walk data.

x_steps = 2*(rand(num_steps) < 0.5) - 1     # generate random steps +/- 1

y_steps = 2*(rand(num_steps) < 0.5) -1

x_coordinate = x_steps.cumsum()            # sum steps to get position

y_coordinate = y_steps.cumsum()


# this function will generate eacah frame of the animation

# it adds all of the data through frame n to a line

# and moves a point to the nth position of the walk

def get_step(n, x, y, this_line, this_point):

      this_line.set_data(x[:n+1],  y[:n+1])

      this_point.set_data(x[n], y[n])


# call the animator and create the movie

my_movie = animation.FuncAnimation(fig, get_step, frames=num_steps, \

                                             fargs=(x_coordinate, y_coordinate, my_line, my_point)   )


# save the movie in the current directory

# *** next line will cause an error unless FFMPEG or MENCODER is installed ***

# my_movie.save('random_walk.mp4', fps=30)
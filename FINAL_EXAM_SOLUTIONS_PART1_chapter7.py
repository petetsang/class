#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Wed Apr 24 10:36:50 2019

@author: pedro brodude
Modified:  Wed Apr 24 10:36:50 2019
Description
____________________

"""

import numpy as np
import matplotlib.pyplot as plt


#STATISTICS OF RANDOM WALKS
#
#WE SHALL GENERATE 2 DIMENSIONAL RANDOM WALKS. PLOT THEIR TRAJECTORIES,
#LOOK AT THE DISTRIBUTION OF END POINTS FOR LARGE NUMBER OF RANDOM WALKERS.
#
#OUR GOALS ARE TO 
#
#1) Generate random walk trajectories that begin at the origin and take random 
#diagonal steps: 
#    
#    x_{n+1} = x_n +/- 1          y_{n+1} = y_n +/- 1              (7.1)
#    
#2) Plot trajectories of four such walks in separate subplots of a single figure.
#3) Plot end point
#4) Compute the average final distance of the walkers from the origin.
#    
#    Review section 6.2


#
#7.1 GENERATING AND PLOTTING TRAJECTORIES
#
#First, let's create a random walk of 1000 steps. each given by Equation 7.1.
#Each trajectory will be a list of 1000 x values, 1000 y values. 
#REMEMBER it's good programming practice to define the size of 

#num_steps = 1000

#Now you can easily set the size of all arrays by using num_steps

#
#Assignment: 
#    a) Use the ideas of Section 6.2 to make a random walk trajectory, and then plot it.
#    To remove any distortion, use the command plt.axis('equal') after making the plot.
#


#    b) Make 4 of these trajectories, and look at all four side by side. Use plt.figure() 
#    to create a new figure window. Access individual subplots by using plt.subplot(2,2,1)
#    before the first plt.plot command. plt.subplot(2,2,2) before the second plot command.
#    Use plt.xlim and/or plt.axes to give your plots same x and y limits.
#    
#    
# Assignment solution:
#From Chapter 6, we remember to get x_position's and y_position's as follows 


#%%
import numpy  as np
import matplotlib.pyplot as plt
from numpy.random import random as rng


max_steps=4000

num_steps = np.arange(1,max_steps+1)
mean_distance=np.zeros(max_steps)
mean_distance_squared=np.zeros(max_steps)



for i in num_steps:
    num_walks = 1000
    
    x_final=np.zeros(num_walks)
    y_final=np.zeros(num_walks)
    distance=np.zeros(num_walks)
    
    for subplot_number in np.arange(1,num_walks):    # preparing 4 subplots
        random_x = rng(i)            # random numbers of x
        random_y = rng(i)            # random numbers for y
        
        true_false_x = (random_x < 0.5)      # anything less than 0.5 is true
        true_false_y = (random_y < 0.5)
        
        x_step = (true_false_x*2)-1          # turn 0,1's into -1,+1's
        y_step = (true_false_y*2)-1
        
        x_position = np.cumsum(x_step)       # cummulative summing -1's +1's into positions
        y_position = np.cumsum(y_step)
        

########################################################################################
### plotting every single random walk. comment this out later when you just need overall 
        # statistics
        
#       plt.subplot(10,10,subplot_number)    # change from plt.subplot(2,2,1) to plt.subplot(2,2,2)...give each plot the same x and y axis limits
        
#        plt.plot(x_position,y_position)
########################################################################################
########################################################################################

    #    plt.xlim(left=-3,right=1)
    #    plt.ylim(top=-10,bottom=10)
    #    plt.axis('equal')
        distance[subplot_number-1] = np.sqrt((x_position[-1]**2+y_position[-1]**2))
        #make a new figure for end points plot
    
        x_final[subplot_number-1] = x_position[-1]
        y_final[subplot_number-1] = y_position[-1]
    mean_distance[i-1]=np.mean(distance)
    mean_distance_squared[i-1]=np.mean(distance**2)
#        print( "num_steps = " + str(i))
    ###### plot number of steps vs mean distance and mean distance^2
    #    print( "\n np.mean(distance) for this " + str(num_steps) + " random walk  =" + str(np.mean(distance))  + "" )
    #    )
#    print( "\n np.mean(distance**2) for this " + str(num_steps) + " random walk  =" + str(np.mean(distance**2))  + "\n" )
#    mean_distance_squared[num_steps]=np.mean(distance**2)


#%%
########
    # plotting over all statistics of random walks
    ##############################################
plt.figure()
plt.subplot(2,2,1)
plt.scatter(np.arange(1,max_steps+1),mean_distance)
ax=plt.gca()
ax.set_xlabel("num_steps")
ax.set_ylabel("mean_distance")
ax.set_title("mean_distance as a function of number of steps in a random walk")
plt.subplot(2,2,2)
plt.scatter(np.arange(1,max_steps+1),mean_distance_squared)
ax=plt.gca()
ax.set_xlabel("num_steps")
ax.set_ylabel("mean_distance^2")
ax.set_title("mean_distance^2 as a function of number of steps in a random walk")
###########




fig =plt.figure()
fig.suptitle("Random walk statistics for " + str(max_steps) + " steps")

plt.subplot(3,2,1)
plt.hist(distance)
plt.ylabel("distance")
plt.xlabel("count")

plt.subplot(3,2,2)
plt.semilogy(distance)
plt.ylabel("log distance")
plt.xlabel("run number")
plt.title("mean distance is "+ str(np.mean(distance)) + "for number of steps = " + str(max_steps) )
#plt.yscale('log',basey=2) 

plt.subplot(3,2,3)
plt.hist(distance**2)
plt.ylabel("distance^2")
plt.xlabel("count")

plt.subplot(3,2,4)
plt.ylabel("log distance^2")
plt.xlabel("run number")
plt.semilogy(distance**2)
plt.title("mean distance^2 is " + str(np.mean(distance**2)))

plt.subplot(3,2,5)
plt.scatter(x_final,y_final)
plt.title("final positions")
plt.xlabel("x position")
plt.ylabel("y position")



    
# run the above several times . the walk is random but still, there is a certain 
# statistics . Let's try to understand this
#%%


#How far does the random walker get after 1000 steps? 
#Or, what is the distance from the starting point (0,0) to the end point (x_1000,y_1000)
#for each of the random walk?
#
# Instead of 4 walks, let's say we want 100. You can manually examine 100 plots but 
#    it would be hard to see the common features. 
#    Let's ask Python to generate these random walks 
#    but only show us the summary. 
#
#
#Easy way is to take the code you wrote above and embed it inside a for loop.
#You could create three arrays: x_final , y_final, and displacement to store
#the ending x, y positions and the distance to the origin.
#Then just before the end of the loop, you could add something like
#
#
#x_final[i] = x[-1]
#y_final[i] = y[-1]
#displacement[i] = np.sqrt(x[-1]**2 + y[-1]**2)
#
#
#You can also solve the problem using vectorized operations instead of a for loop.
#Try to figure out how. The vectorized approach is faster than a loop if the arrays are not 
#too large. , that is if num_walks*num_steps < 10^7
#
#
#
#You can summarize the results in at least three ways. You have a lot of end points
#(x_final, y_final pairs), so you can make a scatter plot by using plt.plot or plt.scatter. 
#alternatively, you can examine the lengths of the final displacement vectors or their squares.


#ASSIGNMENT
#    a) Once you have a code that works, increase the number of random walks from 100 to 1000.(see section 3.3.5)
#    Make a scatter plot of the end points  
#    b) Use plt.hist to make a histogram of the displacement values.
#    c) Make a histogram of the quantity displacement**2
#    d) Your result from (c) may inspire a guess as to the mathematical form of the histogram. 

#    Try semilog and log-log axes to inspire and test your guess.

#    e) Use np.mean to find the average value of displacement**2 (the mean-square displacement) for a random 
#     walk of 1000 steps.
#    f) Find the mean-square displacement (displacement**2) of a 4000-step walk. 

#    If you wish to carry the analysis further, 
#    see if you can determine how the mean-square displacement depends on the number of steps in a random
#    walk.
#    
#    It turns out that random walks are partially predictable after all. Out of all the 
#    randomness comes systematic statistical behavior, partly visible in your 
#    answers to (b-f).
#    
#    Experimental data also agree with these predictions. The random walk, although
#    stripped of much of the complexity of real Brownian motion, nevertheless 
#    captures nontrivial aspect of Nature that are not self-evidence from its 
#    formulation. See if your output qualitatively resembles the 
#    experimental data shown in Figure 7.1 for the diffusion of a micrometer-sized 
#    particle in water.

#%%
    
    
    
    
    



























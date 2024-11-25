#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Fri Apr 26 14:24:09 2019

@author: pedro brodude
Modified:  Fri Apr 26 14:24:09 2019
Description




PLEASE NO PHOTOGRPAHS!
____________________

"""



import numpy as np
import matplotlib.pyplot as plt



# 7.3.1  The Poisson distribution.

#Imagine an extremely unfair coin that lands heads with a probability $\Xi$ equal 
#to 0.08 (not 0.5). Each trial consists of flipping the coin 100 times. 
#you might expect that we'd then get about 8 heads in each trial. Although we could,
#in principle, get as few as 0, or as many as 100.
#
#
#The Poisson distribution is discrete probability distribution that applies to 
#rare events. For our extremely unfair coin, the Poisson distribution 
#predicts that the probability of the coin coming up heads l times in 100 flips is
#
#
#P(l) = exp(-8) * 8**l / l!        (7.2)
#
#
#where l is an integer greater than or equal to 0. 
#
#Assignment:
#    a) Before you start flipping coins, plot this function for some 
#    interesting range of l values. You may find the following helpful:
#        
#       - The factorial function can be imported from scipy.special.


from scipy.special import factorial
l=np.arange(1,100)


p= np.exp(-8)*8**l/factorial(l)



plt.plot(l,p)


#       - You need not take values of l all the way out to infinity. 
#        You will see P(l) quickly gets negligibly small.

#       - In Python, the elements of a vector are always numbers 0,1,2,3...
#       and l is also an integer starting from zero. so l is a good array index.

#       The values of 8**l can get very large - larger than the largest 
#       integer NumPy can store. (NumPy uses 64-bit integers, so the largest number 
#                                 it can store is 2**63-1)
#To avoid numerical overflow --- and erroneous results -- use an array of 
#floats instead of integers. Consult help(np.arange), and read about the 
#dtype keyword argument.

l=np.arange(1,100,dtype=float)


p= np.exp(-8)*8**l/factorial(l)



plt.plot(l,p)

#%%
#b) Perform N coin flip trials, each consisting of 100 flips of a coin that 
#lands head only 8% of the time. [Good practice: Eventually you may want 
#                                 to take N to be a huge number. While developing 
#                                 your code, make it not so huge, say, N=1000,
#                                 so that your code will run fast.]
#


#c) Get Python to count the number of heads, M, for each trial. Then use plt.hist
#to create a histogram of the frequency of getting M heads in N trials. If
#you don't like what you see, consult help(plt.hist).(For example, plt.hist may 
#make a poor choice about how to bin the data.)


from numpy.random import random as rng

N = 1000
trials= np.arange(1,N+1)
# number of heads each trial
M = np.zeros(N)


for i in trials:
    flips = rng(100)
    heads = (flips<=0.08)
    M[i-1] = sum(heads)

    
    
plt.figure()
plt.hist(M,bins=20)





#%%



#d) Make a graph of the Poisson distribution (Equation 7.2 above) multiplied by N.
#What's the most probable outcome? Graph this plot on the same axes as the histogram 
#in (c). 
#
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial
from numpy.random import random as rng

N = 1000

l=np.arange(1,100,dtype=float)

p= N*np.exp(-8)*8**l/factorial(l)



plt.plot(l,p)


trials= np.arange(1,N+1)
# number of heads each trial
M = np.zeros(N)


for i in trials:
    flips = rng(100)
    heads = (flips<=0.08)
    M[i-1] = sum(heads)


plt.hist(M,bins=20)




#%%
#e) Repeat (b-d) for N=1,000,000 (1million), and comment. (THIS MAY TAKE A WHILE))
#

from numpy.random import random as rng

N = 1000000

l=np.arange(1,100,dtype=float)

p= N*np.exp(-8)*8**l/factorial(l)

plt.plot(l,p)




trials= np.arange(1,N+1)
# number of heads each trial
M = np.zeros(N)


for i in trials:
    flips = rng(100)
    heads = (flips<=0.08)
    M[i-1] = sum(heads)


plt.hist(M,bins=20)






#%%
#Click the run button over and over for N=1000, and observe that the distribution is a
#bit different every time, and yet each plot has a general similarity to the others.
#


from numpy.random import random as rng

N = 1000

l=np.arange(1,100,dtype=float)

p= N*np.exp(-8)*8**l/factorial(l)

p1=plt.plot(l,p)





trials= np.arange(1,N+1)
# number of heads each trial
M = np.zeros(N)


for i in trials:
    flips = rng(100)
    heads = (flips<=0.08)
    M[i-1] = sum(heads)


p2=plt.hist(M,bins=20)

plt.show(p1,p2)


#%%


#
#7.3.2 Waiting times.
#
#If we flip our imagined coin once every second, then our string of heads and tails becomes
#a time series called a POISSON PROCESS, or shot noise. Flipping heads is a rare
#event, because $Xi$ =0.08. We expect long strings of tails, punctuated by 
#occasional heads.  This raises an interesting question: After we get a heads,
#how many flips go by before we get the next heads? More precisely,
#what's the distribution of the waiting times from one heads to the next?
#
#
#
#Here is one way to get Python to answer that question. We can make a long list
#of ones and zeros, then search it for each occurrence of a 1 by using
#NumPy's np.nonzero function. 

#This function takes an array of numbers and returns an array of the indices of its nonzero entries. 

#Experiment with small arrays like np.nonzero([1,0,0,-1]) to understand its behavior. Consult help(np.nonzero)
#for more information.
#    

a=np.nonzero([1,0,0,-1,0,0,0,1,123,14,5425,25,0,23])






#%%
#    Each waiting time is the length of a run of zeros , plus one. You
#    can subtract successive entries in the array returned by np.nonzero to find 
#    the waiting time between successive heads, then make a graph showing the 
#    frequencies of these intervals. NumPy's np.diff function will take the 
#    difference of successive entries in an array. Flatten the array returned by
#    np.diff before plotting. See section 2.2.8 for details on flattening arrays. 
#    Consult help(np.diff) for more informatin about that function.
#    
a=np.nonzero([1,0,0,-1,0,0,0,1,123,14,5425,25,0,23])

np.diff(a)



#    Try to guess what this distribution will look like before you compute the 
#    answer. Someone might reason as follows: 
#        "Because heads is a rare outcome, once we get tails we're likely to
#        get a lot of them in a row, so short strings of zeros will be less
#        probable than medium-long strings. But eventually we're bound to get
#        heads, so very long strings of zeros are also less commo than medium-long
#        strings." 
#        Think about it. Is this sound reasoning? Now compute your answer.
#        If your output is not what you expected, try to figure out why.
#        
#        

#%%
#Assignment:
#    a) Construct a random string of 1's and 0's representing 1000 flips of the unfair coin.
#    Then, plot the frequencies of waiting times of length 0,1,2,...., as 
#    outlined above. Also make a semilog plot of these frequencies. Is this 
#    a familiar looking function
#    


from numpy.random import random as rng

num_flips = 1001    #1001 seconds

p = 0.08  # probability of heads

time = np.arange(1,num_flips+1)     #1001 seconds

flips = rng(num_flips)                #1000 flips

heads = (flips<p)       # unfairly, only 8% are heads 
  
string= heads*1              # convert true/false heads to strings of 0's and 1's

a=np.nonzero(string)           # which index is non-zero?

wait_time_diff = np.diff(a)     # difference of these indices = wait time between heads. 


wait_time = wait_time_diff.flatten()+1    # just a technicality because np.diff returns [1,x] array. flatten to [x] array. + 1 cause you count up to next flip
max_wait = wait_time.max()

plt.figure("Short Histogram", figsize=(12,9))

#plt.hist(wait_time,bins=30)                 # what is frequency of wait time?


counts, bin_edges, _ = plt.hist(wait_time ,bins=max_wait//2, range=(0,max_wait))

#plt.semilogy(time,wait_time)              # over the course of flipping, which wait times is most frequent?

plt.semilogy(bin_edges[:-1], counts, 'r.', markersize=10)


plt.xlabel("waiting time between heads", fontsize=16, family='monospace')
plt.title("waiting times in poisson process with p ={}".format(p), fontsize=24)
plt.ylabel("occurances  in {:,d} flips".format(num_flips),fontsize=16)
#    b) What is the average waiting time between heads?


#%%

#    c) Repeat (a) and (b) for 1,000,000 flips of the coin.



from numpy.random import random as rng

num_flips = 10**6    #1001 seconds

p = 0.8  # probability of heads

time = np.arange(1,num_flips+1)     #1001 seconds

flips = rng(num_flips)                #1000 flips

heads = (flips<p)       # unfairly, only 8% are heads 
  
string= heads*1              # convert true/false heads to strings of 0's and 1's

a=np.nonzero(string)           # which index is non-zero?

wait_time_diff = np.diff(a)     # difference of these indices = wait time between heads. 


wait_time = wait_time_diff.flatten()+1    # just a technicality because np.diff returns [1,x] array. flatten to [x] array. + 1 cause you count up to next flip
max_wait = wait_time.max()

plt.figure("Short Histogram", figsize=(12,9))

#plt.hist(wait_time,bins=30)                 # what is frequency of wait time?


counts, bin_edges, _ = plt.hist(wait_time, bins=max_wait//2, range=(0,max_wait), fc=(0, 0, 0, 0.))   # fc gives color

#plt.semilogy(time,wait_time)              # over the course of flipping, which wait times is most frequent?

plt.semilogy(bin_edges[:-1], counts, 'r.', markersize=10)


plt.xlabel("waiting time between heads", fontsize=16, family='monospace')
plt.title("waiting times in poisson process with p ={}".format(p), fontsize=24)
plt.ylabel("occurances  in {:,d} flips".format(num_flips),fontsize=16)




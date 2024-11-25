#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_name.py
# Python 3.7
"""
Created on Sun Apr 28 21:22:29 2019

@author: pedro brodude
Modified:  Sun Apr 28 21:22:29 2019
Description
____________________

"""


# A GUI IS BUILD FROM WIDGETS.
# THE FUNDAMENTAL UNITS USED TO BUILD A GUI IS
# TEXT BOXES (INACTIVE WIDGETS THAT SIMPLY DISPLAY A TEXT MESSAGE)
# ENTRY BOXES   (INTERACTIVE TEXT BOXES FOR USERS TO ENTER TEXT AND NUMBERS)
# BUTTONS (INTERACTIVE REGION OF THE GUI. WHEN USER CLICKS,SOMETHING HAPPENS)

# WIDGETS ARE PACKED INTO FRAMES.

# FRAME IS AN ABSTRACT REGION OF THE GUI OCCUPIED BY A WIDGET OR WIDGETS.

# WE WILL PACK WIDGETS INTO FRAMES BY CREATING A WIDGET, THEN SPECIFYING WHICH FRAME TO PUT IT IN. 'TOP', 
# 'BOTTOM', 'LEFT, 'RIGHT'


# WE CAN PACK FRAMES WITHIN FRAMES. 

# EVENTS TRIGGER ACTIONS

# WHEN WE INTERACT WITH A GUI, WE EXPECT SOMETHING TO HAPPEN. AN EVENT IS SOMETHING THAT HAPPENS WITHIN A GUI:
# PRESS A KEY, PUSH A BUTTON.. GUI PROGRAMMING LINKS EVENTS TO SPECIFIC ACTIONS.



# EVENTS ARE BOUND TO WIDGETS
# WHEN CREATING A GUI, WE BIND EVENTS TO SPECIFIC WIDGETS. 
# IF YOU CREATE A 'PRESS HERE' BUTTON, YOU GET TO ASSIGN THE EVENT "CLICK ON <PRESS HERE> BUTTON"
# TO ANYTHING YOU LIKE: EG, MAKE A SOUND, DISPLAY A MESSAGE, RUN A MONTE CARLO SIMULATION. ETC.


# MAKE A QUICK SKETCH O LAYOUT OF A GUI IS A GOOD IDEA.


# Tkinter is the standard  GUI library for Python and is included in most Python distributions.
# Tkinter provides an object-oriented framework for GUI programming. There are objects like 
# Frame, Label, Entry, and Button that implement the widgets we need. We will build a GUI by
# creating a collection of these objects, then using their methods to adjust their properties and 
# pack them together into a single window.

# let's import Tkinter module.

try:
    # this will work in Python 2.7
    import Tkinter
except ImportError:
    # this will work in Python 3.5
    import tkinter as Tkinter
    
    # for some reason Python 3 uses lower case tkinter.
    
# with the anaconda distribution , if pyplot and Tkinter are to be used in the same program, you 
    # have to instruct PyPlot to use Tk-based back end for displaying plots:
    
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


#%%   
    
# your first GUi
 
# Create main window
root = Tkinter.Tk()
 
# Activate the window
root.mainloop()
 
 # the first command creates an object for the window that will contain the entire GUI
 # this object is a top level widget of Tk which represents mostly the main window
 # of the application.
 
 # this command should probably come near the top of your program. 
 #The second command should come near the end of the program. 
 
 
 
 
 
 
 
 
 #%%
    
 # now let's add the simplest possible widget to our GUI and pack it into the main window
 
 # create main window
root = Tkinter.Tk()
 #create a text box and pack it in
greeting = Tkinter.Label(text="Hello world.")
greeting.pack()
 
 # activate the window
root.mainloop()
 
 
 # note how the widget was created. We created a variable 'greeting' and assigned it to a Tkinter.Label object. 
 # we used the keyword argument 'text="Hello world".  Then we packed this newly created widget into the main window.
 
 #%%%
import tkinter as Tkinter
 # Binding an event to a keystroke
 
 # next we will bind an event to a keystroke within the main window. With the following script,
 # you can now close the window by pressing <Escape> key as long as the window is active
 
 # create main window
root = Tkinter.Tk()
 
 # Create a text box and pack it in
greeting = Tkinter.Label(text="Hello world")
greeting.pack()
 
 # Define a funcction to close the window
def quit(event=None):
     root.destroy()
     
# cause pressing <esc> to close the window
root.bind('<Escape>', quit)
 
 #Activate the window
root.mainloop()
 
 # note you only pass the name of the function to .bind . otherwise you will get an error.
 #
 # some Tkinter methods pass an event object to the function they are given. and some do not
 # to accommodate both types of methods, I gave the function an optional argument with 
 # a default value.
 
 # if you want to bind an event to a mouse click instead of a keystroke, use '<Button-1>'
# as the "key". Add the following lines to the script above , just before the root.mainloop() command:
 
def ring(event=None):
     root.bell()
     
root.bind('<Button-1>', ring)

# now you will hear a beep anytime you click the mouse inside the main window

#%%
# Binding an event to a Widget

# you can also bind events to specific widgets within the main window. Let's add 
# a button to close the window

# create main window
root = Tkinter.Tk()

# create a text box and pack it in
greeting = Tkinter.Label(text="Hello world!!")
greeting.pack()

# define a function to close the window
def quit(event=None):
    root.destroy()
    
# cause pressing <Esc> to close the window
root.bind('<Escape>', quit)


# create a button that will close the window
button = Tkinter.Button(text="Exit", command=quit)
button.pack(side='bottom', fill='both')

# Activate the window
root.mainloop()






# in this example, i have created a button with some text and bound it to the quit() command
# that closes the window. Notice, also that we have provided instructions to where the 
# button is to be placed: side='bottom'. and the button to fill all available space around
# the frame.





#%%

# Entry Boxes, Variables, and Frames

# Now let's look at the last few elements we will need to create a useful GUI


# An entry box allows you to pass information to programs called by the GUI.
# In order for the GUI to keep track of variables it contains, we need to assign the data
# in an entry box to a Tkinter variable.
# Tkinter recognizes several types: IntVar for integers, DoubleVar for floats, 
# StringVar for strings. 

# if you provide an entry box, it is often useful to provide a text box that indicates what 
# the user is entering. this can create a problem for packing.  you want the  entry box 
# to be side by side. but the program that arranges all of our widgets in the main window might not 
# arrange things in an aesthetically pleasing manner. The solution is to pack the textbox and 
# entry box into a separate frame, then pack this frame into the application window.

# you can replace entry boxes with sliders for some variables (look up Tkinter.Scale)
# you can add check boxes for boolean variables (look up Tkinter.Checkbutton )




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

#%%
 
 
 
 
 
import numpy as np
import matplotlib.pyplot as plt

#Binding an Event to a Widget

#You can also bind events to specific widgets within the main window. Let’s add a button to close the window.

# Create main window.
root = Tkinter.Tk()

# Create a text box and pack it in.
greeting = Tkinter.Label(text="Hello, world!")
greeting.pack()

# Define a function to close the window.
def quit(event=None):
    root.destroy()

# Cause pressing <Esc> to close the window.
root.bind('<Escape>', quit)

# Create a button that will close the window.
button = Tkinter.Button(text="Exit", command=quit)
button.pack(side='bottom', fill='both')

# Activate the window.
root.mainloop()

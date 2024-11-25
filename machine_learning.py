#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# machine_learning.py
# Python 3.7
"""
Created on Wed Apr 10 10:57:39 2019

@author: pedro brodude
Modified:  Wed Apr 10 10:57:39 2019
Description
this is directly following machinelearningmastery.com/machine-learning-in-python-step-by-step/

We will use the famous iris flower, where 150 observations of iris flowers are in the dataset.

There are four columns of measurements of the flowers in centimeters.
The fifth column is the species of the flower observed. 
All observed flowers belong to one of three species.

you can learn more about this dataset in wikipedia about iris flower data set

Fisher's iris data set is a multivariate data set introduced by 
Ronald Fisher in 1936 's paper  "the use of multiple measurements in taxonomic problems as an 
example of linear discriminant analysis".
____________________

"""

import numpy as np
import matplotlib.pyplot as plt

import sys
import scipy
import pandas
import sklearn
#%%


# load libraries
import pandas
from pandas.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# load dataset from UCI Machine Learning repository
# We are using pandas (instead of numpy for now) to load data

# we specify the names of each column when loading the data

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

#if you have network connection problems, download the iris.csv file from here:
# ....need to provide file for people to use

# Examine the data
#
print(dataset.shape)
#you should see (150,5)  150 iris flowers, 5 columns


#%%
# it's ALWAYS good practice to look into the data file
# let's look at the first 20 rows
print(dataset.head(20))


#%%

# statistical summary  . this should give the count, mean, min, max values and 
# some basic statistics . The scale is in centimeters.
print(dataset.describe())



#%%
# Class distribution
# let's look at the number of instances (rows) that belong to each class
print(dataset.groupby('class').size())
# for a particular class, we see its size


#%%

# data visualization
# let's look at two types of plots
# 1) Univariate plots to better understand each attribute
# 2) multivariate plots to better understand relations between attributes


# UNIVARIATE PLOTS

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()


#this gives us clearer idea of distribution of the input attributes

#%%

# let's also create a histogram of each input variable to get an idea of the distribution

dataset.hist()
plt.show()
#%%

# two of the input variables have gaussian distribution. This is useful 
# to note as we can use algorithms that can exploit this assumption.


# MULTIVARIATE PLOTS

# let's look at interactions between the variables

# Scatterplots of pairs of attributes  . Help us find relations

scatter_matrix(dataset)
plt.show()

#%%
# note the diagonal grouping of some pairs of attributes. This suggests a high 
# correlation and a predictable relationship



# 5. Evaluate some algorithms
# now it's time to create some models of the data and estimate their accuracy
# on unseen data

# steps
# 1) separate out a validation dataset
# 2) set up a test harness to use 10-fold cross validation
# 3) build 5 different models to predict species from flower measurements
# 4) select best model


# 5.1 Create a validation dataset

# we need to know that the model we created is any good

# later we will use statistical methods to estimate the accuracy of the models


# that is, we are going to hold back some data that the algorithms will not get
# to see and we will use this data to get a second and independent 
# idea of how accurate the best model might actually be


# let's split the dataset into two , 80% of which we will use to train our 
# models and 20% will be used to test 


array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

#%%
# you are now training data in the X_train and Y_train for preparing 
# models and a 
# X_validation and Y_validation sets that we can use later


# 5.2 TEST HARNESS

# split our dataset into 10 parts, train 9, test 1 and repeat for all combinations
# of train-test splits


seed = 7
scoring = 'accuracy'


# the specific random seed does not matter. learn more about pseudorandom number generators on your own

# we use the metric 'accuracy' to evaluate models. 
# this is a ratio of number of correct divided by total number, in percentage



# 5.3  BUILD MODELS


# which algorithm would be good? what configurations to use?
# let's evaluate 6 different algorithms


# Logistic Regression (LR)  (linear algorithm)
# Linear Discriminant Analysis (LDA)  (linear algorithm)
# K-Nearest Neighbors (KNN)   (non-linear algorithm)
# Classification and Regression Trees (CART) (non-linear algorithm)
# Gaussian Naive Bayes (NB)   (non-linear algorithm)
# Support Vector Machines (SVM)   (non-linear algorithm)


# we reset the random number seed before each run to ensure that the evaluation
# of each algorithm is performed using exatly the same data splits.

#%%

# let's build and evaluate our models

models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

results =[]
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

#%%


# 5.4 Select Best Model

# we have 6 models and accuracy estimations for each.  let's select the most accurate
    
    
# after the above run, we see that Support Vector Machines (SVM) has the highest accuracy
    
#let's create a plot of the model evaluation results and compare the spread and accuracy of each model.
    
    
# there is a population of accuracy measures for each algorithm because each algorithm was evaluated 10 times (10 fold cross validation)
    
# COMPARE ALGORITHMS
    
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

# you will see that man samples acheieve 100% accuracy.


#%%
# 6.  MAKE PREDICTIONS

# THE KNN algorithm is very simple and was an accurate model based on our tests.
# let's get an idea of the accuracy of the model on our validation set

# this will give us an independent final check. 
# you should keep a validation set just in case you made a slip during training. such as overfitting the 
# to the training set or a data leak. Both will result in an  overly optimistic result.

# let's run the KNN model directly on the validation set 


# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))







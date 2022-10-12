#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 14:48:40 2022

@author: paola_amigo
""" 

print ('Hello, World!')

import csv
import sys

# Part 1
f = open('TB_burden_countries_2014-09-29.csv') # opens the csv file

# 1. Count the number of rows in the csv file you've chosen.
    
total = 0
for row in csv.reader(f):
    total+=1
print(total)

# Part 2
import numpy as np

#Create an array of int ranging from 5-15
a= np.arange(5,16)
print(a)

#Create an array containing 7 evenly spaced numbers between 0 and 23
b= np.linspace(0,23,7)
print(b)

#Numpy has several routines for generating artificial data following a particular structure. Check this page for different types. And generate an artificial numpy array with values between -1 and 1 that follow a uniform data distribution.
u= np.random.random_sample(10)
print(u)

#Visualise the array in an histogram in matplotlib.
import matplotlib.pyplot as plt

plt.hist(u)
plt.show()

#Create two random numpy arrays with 10 elements. Find the Euclidean distance between the arrays using arithmetic operators, hint: numpy has a sqrt function
p= np.random.random(10)
q= np.random.random(10)

e= np.sqrt((sum(p-q))**2)
print(e)

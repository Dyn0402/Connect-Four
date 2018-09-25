# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 20:38:27 2018

@author: Dylan
"""

import numpy as np
from scipy.special import expit


def ActFunc(x, func='ReLU'):
    if(func.lower() == 'identity'):
        return(identity(x))
    if(func.lower() == 'relu'):
        return(reLU(x))
    elif(func.lower() == 'tanh'):
        return(tanh(x))
    elif(func.lower() == 'sigmoid'):
        return(sigmoid(x))
    else:
        print('Activation Function not available.')
        return(x)

def identity(x):
    return(x)

def didentity(x):
    return(0)

def reLU(x):
    return(max(0,x))
    
def dreLU(x):
    return(max(0,x)/x)
    
def tanh(x):
    return(np.tanh(x))
    
def dtanh(x):
    return(np.cosh(x)**-2)
    
def sigmoid(x):
    return(expit(x))
    
def dsigmoid(x):
    y = sigmoid(x)
    return(y * (1 - y))
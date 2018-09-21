# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 20:38:27 2018

@author: Dylan
"""

import numpy as np
from scipy.special import expit


def ReLU(x):
    return(max(0,x))
    
def tanh(x):
    return(np.tanh(x))
    
def sigmoid(x):
    return(expit(x))
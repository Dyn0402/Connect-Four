# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:27:30 2018

@author: Dylan
"""

import ActivationFunction as AF


class Neuron:
    def __init__(self, nextNeurons, value=0.0):
        self.nextNeurons = nextNeurons
        self.value = value
        
    def fire(self, func='relu'):
        actVal = AF.ActFunc(self.value, func=func)
        for i in range(len(self.nextNeurons['connections'])):
            val = self.nextNeurons['connections'][i].getValue()
            dval = self.nextNeurons['weights'][i] * actVal
            self.nextNeurons['connections'][i].setValue(val + dval)
            
    def setValue(self, x):
        self.value = x
        
    def getValue(self):
        return(self.value)
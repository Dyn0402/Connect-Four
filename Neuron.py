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
        
    def fire(self):
        actVal = AF.ReLU(self.value)
        for neuron, weight in self.nextNeurons.items():
            neuron.value += actVal*weight
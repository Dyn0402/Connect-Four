# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:36:23 2018

@author: Dyn04
"""

import NetIO as NIO
import NetBuild as NB


class NeuralNet:
    #layers array with number of neurons in each layer.
    #layer[0] input layer
    #layer[-1] output layer
    #layer[i] number of neurons in ith layer
    def __init__(self, netPath = '', layers = []):
        if netPath != '':
            pass
        else:
            neurons = NB.buildNet(layers)
        
        self.numLayers = len(self.neurons)
        
            
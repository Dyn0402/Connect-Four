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
        self.path = netPath
        if layers != []:
            self.net = NB.buildNet(layers)
            if self.path != '':
                NIO.createNetFile(self)
        else:
            if self.path != '':
                NIO.loadNetFile()
            else:
                self.net = NB.buildNet(layers) #Empty object if no params given to init.
        
        self.numLayers = len(self.net)
        self.output = [outNeuron.value for outNeuron in self.net[-1]]
        
        
    def fireNet(self, func='relu'):
        for neuron in self.net[0]:
            neuron.fire(func='identity')
        for layer in self.net[1:-1]:
            for neuron in layer:
                neuron.fire(func=func)
                
        self.output = [outNeuron.value for outNeuron in self.net[-1]]
    
    
    #Not functional method.    
    def updateWeights(self):
        for layer in self.net:
            for neuron in layer:
                for connection in neuron.nextNeurons:
                    newWeight = updateConnection() ################################
                    neuron.nextNeurons[connection] = newWeight
                    
    
    def updateInput(self, newInputs):
        if(len(newInputs) != len(self.net[0])):
            print('Input layer dimension mismatch. Input neurons not updated.')
        else:
            for i in range(len(self.net[0])):
                self.net[0][i].value = newInputs[i]
                
                
    def getOutput(self):
        return(self.output)
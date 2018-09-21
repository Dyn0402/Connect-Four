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
            self.neurons = NB.buildNet(layers)
            if self.path != '':
                NIO.createNetFile(self)
        else:
            if self.path != '':
                NIO.loadNetFile()
            else:
                self.neurons = NB.buildNet(layers) #Empty object
        
        self.numLayers = len(self.neurons)
        self.output = [outNeuron.value for outNeuron in self.neurons[-1]]
        
        
    def doTheThing(self):
        getInput(self.neurons[0]) #################################################
        for layer in self.neurons[:-1]:
            for neuron in layer:
                neuron.fire()
                
        self.output = [outNeuron.value for outNeuron in self.neurons[-1]]
        
        
        
    def updateWeights(self):
        for layer in self.neurons:
            for neuron in layer:
                for connection in neuron.nextNeurons:
                    newWeight = updateConnection() ################################
                    neuron.nextNeurons[connection] = newWeight
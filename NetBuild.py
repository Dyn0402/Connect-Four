# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 19:13:23 2018

@author: Dylan
"""


import Neuron


#Build network of neurons.
#Start with last (output) layer and continue backward to input layer,
#making connectections between each layer.
def buildNet(layers, startWeight = 1.0):
    neurons = []
    for layer in layers[::-1]:
        if len(neurons) > 1:
            nextNeurons = []
        else:
            nextNeurons = zip(neurons[-1], len(neurons[-1])*[startWeight])
        neurons.append([])
        for neuron in range(layer):
            neurons[-1].append(Neuron.Neuron(nextNeurons))
    
    neurons.reverse() #Start with inputs end with outputs.
    
    return(neurons)
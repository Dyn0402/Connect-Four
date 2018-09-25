# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 19:13:23 2018

@author: Dylan
"""


import Neuron
import scipy.stats as stats
from random import random


#Build network of neurons.
#Start with last (output) layer and continue backward to input layer,
#making connectections between each layer.
def buildNet(layers):
    neurons = []
    for layer in layers[::-1]:
        nextNeurons = {'connections':[], 'weights':[]}
        if len(neurons) < 1:
            connections = [] #If output layer, no connections.
        else:
            connections = neurons[-1]
        neurons.append([])
        for neuron in range(layer):
            for connection in range(len(connections)):
                nextNeurons = {'connections':connections, 'weights':[random() for i in range(len(connections))]} #Change to Gaussian rather than linear distribution.
            neurons[-1].append(Neuron.Neuron(nextNeurons))
    
    neurons.reverse() #Start with inputs end with outputs.
    
    return(neurons)
    
    
#net = buildNet([3,4,2])
#for layer in net:
#    print('layer')
#    for neuron in layer:
#        print('neuron')
#        print(len(neuron.nextNeurons['weights']))
#        print(neuron.nextNeurons['weights'])
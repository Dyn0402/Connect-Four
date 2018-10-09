# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 16:21:04 2018

@author: Dyn04
"""

import NeuralNet as NN
import ActivationFunction as AF

def main():
    xOrNet = NN.NeuralNet(layers=[2,3,1])
    inpt = [1,1]
    outpt = [0]
    
    xOrNet.updateInput(inpt)
    
    setInitialWeights(xOrNet)
    
    xOrNet.fireNet(func='sigmoid')
    print(AF.sigmoid(xOrNet.getOutput()))
    
    erOut = 0.0 - AF.sigmoid(xOrNet.getOutput())
    dOut = AF.dsigmoid(xOrNet.getOutput()) * erOut
    
    print(dOut)
    
    
    
    
    
    
def setInitialWeights(Net):        
    Net.net[0][0].nextNeurons['weights'] = [0.8, 0.4, 0.3]
    Net.net[0][1].nextNeurons['weights'] = [0.2, 0.9, 0.5]
    
    Net.net[1][0].nextNeurons['weights'] = [0.3]
    Net.net[1][1].nextNeurons['weights'] = [0.5]
    Net.net[1][2].nextNeurons['weights'] = [0.9]
            
    


if __name__ == '__main__':
    main()
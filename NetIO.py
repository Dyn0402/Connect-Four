# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:15:02 2018

@author: Dylan
"""

import os
import pickle


def createNetFile(self):
    if os.path.exists(self.path):
        overwrite = input('NetFile already exists, overwrite (otherwise proceed without saving)? [y]/[n]')
        if overwrite != 'y':
            self.path = ''
            return()
    pickle.dump(self.neurons, open(self.path, 'wb'))
    

def loadNetFile(self):
    self.neurons = pickle.load(open(self.path, 'rb'))


def updateNetFile(self):
    pickle.dump(self.neurons, open(self.path, 'wb'))
    

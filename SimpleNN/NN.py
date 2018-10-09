
import numpy as np

class NN:
    def __init__(self,layerSizes,learnRate,gamma,sigma,dsigma):

        assert(len(layerSizes) >= 2) # require at least input and output layer

        self.learnRate = learnRate  # learning rate (gradient descent)
        self.gamma = gamma  # regularizer coeff for weights
        self.sigma = sigma  # activation function
        self.dsigma = dsigma  # derivative of activate

        self.weights = [(np.random.rand(layerSizes[i+1],layerSizes[i])-0.5)*self.learnRate for i in range(0,len(layerSizes)-1)]
        self.layerVals = [None for i in layerSizes]
        self.dLoss = [None for i in layerSizes]

    def forwardProp(self,inputVals):

        self.numTrials = inputVals.shape[1]
        assert(inputVals.shape[0] == self.weights[0].shape[1])
        self.layerVals[0] = inputVals

        i = 0
        for weightMat in self.weights:
            self.layerVals[i+1] = self.sigma(np.matmul(weightMat,self.layerVals[i]))
            i += 1

        return self.layerVals[-1]

    def backProp(self,groundTruth,verbose = False):
        # expect ground truth in format (#classes) x (#trials) with 0 or 1
        assert(groundTruth.shape == self.layerVals[-1].shape)

        # Set dLoss for output layer. This is gradient of loss function
        # w.r.t. output layer values.
        self.dLoss[-1] = self.layerVals[-1] / np.sum(self.layerVals[-1],axis = 0) - groundTruth
        if(verbose):
            print('\n\n\n Outlayer dLoss: {}'.format(self.dLoss[-1]))

        # Iterate backwards over layers. Set weights[i] based on dLoss[i+1],
        # then use this to calculate dLoss[i]
        for i in reversed(range(0,len(self.layerVals)-1)):
            temp = self.dLoss[i+1]*self.dsigma(self.layerVals[i+1])
            temp2 = np.matmul(temp,self.layerVals[i].transpose())
            self.weights[i] -= self.learnRate*(temp2/self.numTrials + self.gamma*self.weights[i])
            self.dLoss[i] = np.matmul(self.weights[i].transpose(),
                                      self.dLoss[i+1]*self.dsigma(self.layerVals[i+1]))
            if(verbose):
                print('\n weight gradient: {}'.format(temp2))
                print('\n dLoss layer {}: {}'.format(i,self.dLoss[i]))
            
    def printAll(self):
        for i in range(0,len(self.layerVals)):
            print('layer {}: {}'.format(i,self.layerVals[i]))
            if(i < len(self.layerVals)-1):
                print('weights {} -> {}: {}'.format(i,i+1,self.weights[i]))

    def classify(self):
        return self.layerVals[-1] == np.amax(self.layerVals[-1], axis = 0)

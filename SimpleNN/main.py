
from NN import NN
import numpy as np

# My data maker function
def makeData(numPoints):
    numPoints = int(numPoints/3)
    theta = np.random.rand(1,numPoints)
    theta.sort()
    r = theta*(1 + np.random.rand(1,numPoints)/8)
    theta *= np.pi / 2

    temp = np.concatenate((r*np.cos(theta),r*np.sin(theta)),axis=0)
    
    finalData = np.concatenate(
        (np.concatenate((r*np.cos(theta),r*np.sin(theta)),axis=0),
         np.concatenate((r*np.cos(theta+2*np.pi/3),r*np.sin(theta+2*np.pi/3)),axis=0),
         np.concatenate((r*np.cos(theta+4*np.pi/3),r*np.sin(theta+4*np.pi/3)),axis=0),
        ), axis = 1)

    groundTruth = np.repeat(np.array([[1,0,0],[0,1,0],[0,0,1]]),numPoints,axis = 1)
    
    return [finalData, groundTruth]


##### parameters

layerSizes = [2,4,4,3]
learnRate = 1.0e0
gamma = 1.0e-4    # This is coeff on regularizer term
def sigma(x):         # Activation function
    return 1/(1+np.exp(-x))
def dsigma(x):
    return (1/(1+np.exp(-x))) * (1 - 1/(1+np.exp(-x)))
trainingRuns = 2000

##### Create data
numTrainPoints = 3000  # must be divisible by 3 for this example
numTestPoints = 3000
inDataDim = layerSizes[0]
trainData, groundTruth = makeData(numTrainPoints)
trainData = trainData - np.mean(trainData,axis=1).reshape(2,1)
testData, testGT = makeData(numTestPoints)

##### initialize Neural Net
theNN = NN(layerSizes,learnRate,gamma,sigma,dsigma)

##### Do some stuff
theNN.forwardProp(trainData)
for i in range(0,trainingRuns):
    theNN.backProp(groundTruth)
    theNN.forwardProp(trainData)

finalClasses = theNN.classify()
print(np.sum(np.sum(np.not_equal(finalClasses,groundTruth)))/2)

theNN.forwardProp(testData)
finalClasses = theNN.classify()
print(np.sum(np.sum(np.not_equal(finalClasses,testGT)))/2)

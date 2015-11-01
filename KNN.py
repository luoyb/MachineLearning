__author__ = 'luoyb'

from numpy import  *
import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet() :
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k) :
    dataSetSizes = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSizes,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k) :
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename) :
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataSet) :
    # newValue = (oldValue - min) / (max - min)
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals -  minVals
    normDataSet = zeros((shape(dataSet)))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet / tile(ranges,(m,1))
    return normDataSet,ranges,minVals




'''
test
/Users/luoyb/Downloads/machinelearninginaction/Ch02/datingTestSet2.txt
'''
#group,labels = createDataSet()
#print classify0([1,10],group,labels,3)

filename = '/Users/luoyb/Downloads/machinelearninginaction/Ch02/datingTestSet2.txt'
datingDataMat,datingLabels = file2matrix(filename)
normMat,ranges,minVals = autoNorm(datingDataMat)

def test1() :
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(normMat[:,0],normMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
    fig.show()



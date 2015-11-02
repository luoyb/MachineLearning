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

def datingClassTest() :
    hoRatio = 0.1
    datingDataMat,datingLabels = file2matrix(filename)
    normMat,ranges,minvals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs) :
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],\
                                     datingLabels[numTestVecs:m],3)
        print "the classifier came back with: %d,the real answer is: %d" \
              % (classifierResult,datingLabels[i])
        if(classifierResult != datingLabels[i]) : errorCount += 1.0
    print "the total error rate is: %f" % (errorCount/float(numTestVecs))

def classifyPerson() :
    resultList = ['not at all','in small doses','in large doses']
    percentTats = float(raw_input(\
                        "percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequent flier miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingDatamat,datingLabels = file2matrix(filename)
    normMat,ranges,minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify0((inArr-\
                                 minVals)/ranges,normMat,datingLabels,3)
    print "You will probably like this person: ",\
                        resultList[classifierResult - 1]

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



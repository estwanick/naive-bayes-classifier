import sys
from math import sqrt

datafile = sys.argv[1]
f = open(datafile)
data = []
i = 0
l = f.readline()

# Read data
while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()

# Read labels
labelFile = sys.argv[2]
f = open(labelFile)
trainLabels = {}
labelsSuccess = []
labelsSuccess.append(0)
labelsSuccess.append(0)
l = f.readline()
while(l != ''):
    a = l.split()
    trainLabels[int(a[1])] = int(a[0])
    l = f.readline()
    labelsSuccess[int(a[0])] += 1

# print data

# compute means
nmFailed = []
nmSuccess = []
for j in range(0, cols, 1):
    nmFailed.append(1)
    nmSuccess.append(1)

for i in range(0, rows, 1):
    for j in range(0, cols, 1):
        if(trainLabels.get(i) != None and trainLabels[i] == 1):
            nmSuccess[j] = nmSuccess[j] + data[i][j]
        if(trainLabels.get(i) != None and trainLabels[i] == 0):
            nmFailed[j] = nmFailed[j] + data[i][j]

for j in range(0, cols, 1):
    nmFailed[j] = nmFailed[j]/labelsSuccess[0]
    nmSuccess[j] = nmSuccess[j]/labelsSuccess[1]

#Computing variance
successVariance = []
failureVariance = []
for j in range(0, cols, 1):
    successVariance.append(0)
    failureVariance.append(0)

for i in range(0, rows, 1):
    for j in range(0, cols, 1):
        if(trainLabels.get(i) != None and trainLabels[i] == 1):
            successVariance[j] = (data[i][j] - nmSuccess[j]) ** 2
        if(trainLabels.get(i) != None and trainLabels[i] == 0):
            failureVariance[j] = (data[i][j] - nmFailed[j]) ** 2

# print successVariance
# print failureVariance

for i in range(0, rows, 1):
    feature_predictions = {}
    if(trainLabels.get(i) == None):
        nbF, nbS = 0, 0
        for j in range(0, cols, 1):
            sdF = sqrt(failureVariance[j])
            sdS = sqrt(successVariance[j])
            cell = data[i][j]
            nbF = nbF + (( cell - nmFailed[j] ) / sdF) ** 2
            nbS = nbS + (( cell - nmSuccess[j] ) / sdS) ** 2

        if(nbF < nbS):
            print('0', i)
        else:
            print('1', i)


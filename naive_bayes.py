import sys

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
    nmFailed.append(0)
    nmSuccess.append(0)

failedLabels = 0
successLabels = 0
for i in range(0, rows, 1):
    for j in range(0, cols, 1):
        if(trainLabels.get(i) != None and trainLabels[i] == 1):
            nmSuccess[j] = nmSuccess[j] + data[i][j]
        if(trainLabels.get(i) != None and trainLabels[i] == 0):
            nmFailed[j] = nmFailed[j] + data[i][j]


for j in range(0, cols, 1):
    nmFailed[j] = nmFailed[j]/labelsSuccess[0]
    nmSuccess[j] = nmSuccess[j]/labelsSuccess[1]

# print(nmFailed)
# print(nmSuccess)

# print labelsSuccess[0]
# print labelsSuccess[1]

#Classify points
for i in range(0, rows, 1):
    feature_predictions = {}
    if(trainLabels.get(i) == None):
        d0, d1 = 0, 0
        for j in range(0, cols, 1):
            d0 = d0 + ( nmFailed[j] - data[i][j]**2)
            d1 = d1 + ( nmSuccess[j] - data[i][j]**2)
            if feature_predictions.get(i) is None:
                feature_predictions[i] = []    
            if(d0 < d1):
                # print('0', i)
                feature_predictions[i].append('0')
            else:
                # print('1', i)
                feature_predictions[i].append('1')

        print feature_predictions
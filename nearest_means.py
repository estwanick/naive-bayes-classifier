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
n = []
n.append(0)
n.append(0)
l = f.readline()
while(l != ''):
    a = l.split()
    trainLabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1

# print data
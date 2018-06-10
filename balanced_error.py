import sys
import os

label_path = sys.argv[1]
f = open(label_path)
actual = []
i = 0
line = f.readline()

while(line != ''):
    a = line.split()
    actual.append(int(a[0]))
    line = f.readline()

prediction_path = sys.argv[2]
f = open(prediction_path)
i = 0
line = f.readline()

prediction = [None] * (len(actual) + 1)
while(line != ''):
    a = line.split()
    prediction[int(a[1])] = int(a[0])
    line = f.readline()

a, b, c, d = 0.0, 0.0, 0.0, 0.0
for i in range(0, len(actual), 1):
    if actual[i] == 0 and prediction[i] == 0:
        a = a + 1
    if actual[i] == 0 and prediction[i] == 1:
        b = b + 1
    if actual[i] == 1 and prediction[i] == 0:
        c = c + 1
    if actual[i] == 1 and prediction[i] == 1:
        d = d + 1

f_class = b / (a+b)
s_class = c / (c+d)
balanced_error = 0.5 * (f_class + s_class)

print balanced_error
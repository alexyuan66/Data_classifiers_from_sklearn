#!/usr/bin/python
import random

in1 = open('iris.data', 'r')
out1 = open('iris_training.data', 'w')
out2 = open('iris_testing.data', 'w')

c = 0
c1 = 0
c2 = 0
while c < 145 :
    a = in1.readline()
    c = c+1
    if random.randint(1, 101) < 67 :
        c1 = c1+1
        out1.write(a)
    else :
        c2 = c2+1
        out2.write(a)

for i in range(c1, 100) :
    a = in1.readline()
    out1.write(a)

for i in range(100+c2, 150) :
    a = in1.readline()
    out2.write(a)
    
in1.close()
out1.close()
out2.close()


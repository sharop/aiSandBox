import random
from nt import read
a= 0.05
b= 0.75 + a
c= 0.20 + b

dist = [0.05,0.15,0.15,0.15,0.15,0.15,0.10,0.10]

def eje():
    for i in range(60):
        rdNum = random.random()
        if rdNum < a :
            print 'A'
        elif rdNum < b :
            print 'B'
        else:
            print 'C'

eje()
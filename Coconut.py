#Write a program that will find the initial number
#of coconuts. 
a=[]
m=[]
def f(n):
    return (n-1) / 5.0 *4

def f6(n,log):
    for i in range(6):
        n = f(n)
        if(log):a.append(n)
    if(log):m.append(a)
    return n 

def is_int(n):
    return abs(n-int(n)) < 0.0000001

n=[]   
for i in range(1,100000,1):
    if is_int(f6(i,0)):
        n.append(i)
        m.append(i)
        f6(i,1)

print m
print n
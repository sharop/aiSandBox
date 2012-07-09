## Define a procedure, find_last, that takes as input
## two strings, a search string and a target string,
## and outputs the last position in the search string
## where the target string appears, or -1 if there
## are no occurences.
##
## Example: find_last('aaaa', 'a') returns 3

## Make sure your procedure has a return statement.

#def find_last(a,b):
#    idx=-1
#    acc=-1
#    stop = 0
#    while stop==0:
#        idx = a.find(b,idx+1)
#        if idx==-1:
#            stop=1
#        else:
#            acc=idx                    
#    return acc
        
#def print_multiplication_table(n):
#    
#    for i in range(n):
#        for j in range(n):
#            print  str(i+1) + " * " + str(j+1) + " = " + str((i+1)*(j+1))
#    
#    
#print_multiplication_table(5)

# Write a program that will iteratively update and
# predict based on the location measurements 
# and inferred motions shown below. 

def update(mean1, var1, mean2, var2):
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0
sig = 10000

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig]. 

for i in range(len(measurements)):
    [mu, sig] = update(mu,sig,measurements[i],measurement_sig)
    print 'UPDATE ', [mu, sig]
    [mu, sig] = predict(mu,sig,motion[i], motion_sig)
    print 'PREDICT ', [mu, sig]



print [mu, sig]

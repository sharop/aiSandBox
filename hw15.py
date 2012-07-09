
colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7
sensor_wrong = 1 - sensor_right 
p_move = 0.8
p_stay = 1 - p_move




def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT
#MOVE->Measure
def move(p, movement):    ###Total Probability
    q = []
    for r in range(len(p)):
        inter=[]
        for e in range(len(p[r])):
            #s = p_move * p[(r-movement[0])%len(p)][(e-movement[1])%len(p[r])]
            s = p_move * p[(r-movement[0]%len(p))][(e-movement[1])%len(p[r])] +(p_stay * p[r][e])  
            #              P(Xjt-1))
            #Probabilidad despues del movimiento S---> P(Xi)
            inter.append(s)
        q.append(inter)
    return q

def sense(p, Z):
    q=[]
    s =0
    for i in range(len(p)):
        h=[]
        for c in range(len(p[i])):
            hit = (Z == colors[i][c])
            nn= p[i][c] * (hit * sensor_right + (1-hit) * (sensor_wrong))  # P(Xi)* P(Z|Xi)
            s+=nn
            h.append(nn)
        q.append(h)
           
    for i in range(len(q)):        
        for c in range(len(q[i])):
            q[i][c] /= s
    return q

p = []
if len(measurements) != len(motions):
    raise ValueError, "Error en el tamano del vector measurement y motions"

pinit = 1/float(len(colors))/float(len(colors[0]))
p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]

for k in range(len(measurements)):
    p = move(p, motions[k])
    p = sense(p,measurements[k])
    




#Your probability array must be printed 
#with the following code.

show(p)




text = "first hoo" 
text.index('hoo')


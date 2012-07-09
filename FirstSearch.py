# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1
clos=[]
def search():
    closed=[[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]]=1
    x = init[0]
    y = init[1]
    g = 0
    open = [[g, x, y]]
    found = False # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while found is False and resign is False:
        if len(open) == 0:
            resign = True
            print 'Fail'
        else:
            open.sort()
            open.reverse()
            path = open.pop()
            x= path[1]
            y= path[2]
            g= path[0]

            if x==goal[0] and y==goal[1]:
                found = True
                print path
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
    return path # you should RETURN your result


search()
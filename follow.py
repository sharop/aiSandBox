# -----------
# User Instructions:
# 
# Modify the function search() so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# For grading purposes, please leave the return
# statement at the bottom.
# ----------


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1


# ----------------------------------------
# modify code below
# ----------------------------------------

def search():
    print 'Grid\n '
    for i in  range(len(grid)):
        print grid[i]

    track = 0
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    trackPath = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    gaction = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    
    closed[init[0]][init[1]] = 1
    expand[init[0]][init[1]] = track
    
    
    x = init[0]
    y = init[1]
    g = 0
    gaction[init[0]][init[1]] = g
    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                gaction[x][y]=g
                trackPath[x][y] = '*'
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            track +=1
                            expand[x2][y2] = track
                            action[x2][y2] = i
                            trackPath[x][y]=delta_name[i]
                            gaction[x][y]=g
    

    print 'Gaction \n'
    for i in  range(len(gaction)):
        print gaction[i]
    print 'Action \n'
    for i in  range(len(action)):
        print action[i]
    print 'Track \n'
    for i in  range(len(trackPath)):
        print trackPath[i]

    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]                    
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'

    while x >= init[0] and y >= init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        if gaction[x2][y2] != -1 and gaction[x][y] - gaction[x2][y2] == 1 :
            policy[x2][y2] = delta_name[action[x][y]]
        x= x2
        y=y2    
    print 'Policy\n '
    for i in  range(len(policy)):
        print policy[i]

    return expand #Leave this line for grading purposes!


print search()

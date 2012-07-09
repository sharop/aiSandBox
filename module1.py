#Same Structure

#Define a procedure, same_structure, that takes two inputs. It should output
#True if the lists contain the same elements in the same structure, and False
#otherwise. Two values, p and q have the same structure if:

#    Neither p or q is a list.

#    Both p and q are lists, they have the same number of elements, and each
#    element of p has the same structure as the corresponding element of q.


#For this procedure, you can use the is_list(p) procedure from Homework 6:

def is_list(p):
    return isinstance(p, list)


def same_structure(a,b):
    if not is_list(a) and not is_list(b):
        return True
    elif is_list(a) and is_list(b) and (len(a)==len(b)):
        accBel = True        
        for i,j in zip(a,b):
            if (is_list(i) and is_list(j)) and (len(i)==len(j)):
                accBel = accBel and same_structure(i,j)
            elif (is_list(i) and is_list(j)):
                return False
            else:
                accBel = accBel and same_structure(i,j)
        return accBel
    else:
        return False

def reverse_index(dict):
    wbc={}
    for k,v in dict.iteritems():
        if(wbc.has_key(v)):
            wbc[v].append(k)
        else:
            wbc[v]=[k]
    return wbc


#Reachability

#Single Gold Star

#Define a procedure, reachable(graph, node), that takes as input a graph and a
#starting node, and returns a list of all the nodes in the graph that can be
#reached by following zero or more edges starting from node.  The input graph is
#represented as a Dictionary where each node in the graph is a key in the
#Dictionary, and the value associated with a key is a list of the nodes that the
#key node is connected to.  The nodes in the returned list may appear in any
#order, but should not contain any duplicates.

reach=[]
def reachable(graph, node):
    if(node not in reach):
        reach.append(node)
    for vtx in graph[node]:
        if(vtx not in reach):
            reachable(graph,vtx)
    return reach

#For example,

graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}

#print reachable(graph, 'a')
##>>> ['a', 'c', 'd', 'b']

#print reachable(graph, 'd')
##>>> ['d', 'a', 'c', 'b']

#print reachable(graph, 'e')
##>>> ['e', 'a', 'c', 'd', 'b']

#print reachable(graph, 'b')


def edit_distance(s,t):
  d=dict()
  for i in range(len(s)+1):
     d[i]=dict()
     d[i][0]=i
  for i in range(len(t)+1):
     d[0][i] = i
  for i in range(1, len(s)+1):
     for j in range(1, len(t)+1):
        d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not s[i-1] == t[j-1]))
  return d[len(s)][len(t)]


# Delete the 'a'
print edit_distance('audacity', 'udacity')
#>>> 1

# Delete the 'a', replace the 'u' with 'U'
print edit_distance('audacity', 'Udacity')
#>>> 2

# Five replacements
print edit_distance('peter', 'sarah')
#>>> 5

# One deletion
print edit_distance('pete', 'peter')
#>>> 1

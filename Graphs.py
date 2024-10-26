"""
Graphs
"""

#Directed
n = 8
A = [[0,1], [1,2], [0,3], [3,4], [3,6], [3,7], [4,2], [4,5], [5,2]] #Adjacency List

"""
Converting and array of edges into an adjacency matrix.
"""
M = []
for i in range(n):
    M.append([0]*n)

for u, v in A:
    M[u][v] = 1 
    
    # Uncomment the next line for undirected edges 
    # M[v][u] = 1

# print(M)

"""
Converting an array of edges in to and adjacency list.
"""
from collections import defaultdict

D = defaultdict(list) #Makes the default value of type list

for u, v in A:
    D[u].append(v)

    # Uncomment the next line to make and adjacency list for an undirected graph
    # D[v].append(u)
# print(D)

"""
DFS with recursion. Time complexity: O(V+E), Space complexity: O(V+E) where V is the number of vertices and E is the number of edges.
"""

def recursive_dfs(node):
    print(node) #processing

    for neig_node in D[node]:
        if neig_node not in seen:
            seen.add(neig_node)
            recursive_dfs(neig_node)

source = 0 
seen = set()
seen.add(source)

# recursive_dfs(source)

"""
DFS - iterative.
"""

source = 0
seen = set()
seen.add(source)
stk = [source]

while stk:
    node = stk.pop()
    print(node)
    
    for neig_node in D[node]:
        if neig_node not in seen:
            seen.add(neig_node)
            stk.append(neig_node)

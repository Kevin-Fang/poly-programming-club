from sys import stdin
from collections import defaultdict

# read input for num edges, num nodes
num_nodes, num_edges = stdin.readline().split(" ")
if num_nodes == num_edges == 0:
    print("YES")

# create edge list from input
edge_list = []
for i in range(int(num_edges)):
    first, second = input().split(" ")
    edge_list.append((first, second))

# create adjacency list
node_connections = defaultdict(list)

for first, second in edge_list:
    node_connections[first].append(second)
    node_connections[second].append(first)

# depth first search functions
def depth_first_helper(node, visited, graph):
    visited[int(node)] = True
    for i in graph[node]:
        if visited[int(i)] == False:
            depth_first_helper(i, visited, graph)

def depth_first(node, graph):
    visited = [False] * (len(graph) + 1)
    depth_first_helper(node, visited, graph)
    return visited

# determine if tree
if int(num_edges) != int(num_nodes) - 1:
    print("NO")
else:
    visited = depth_first('1', node_connections) 
    for i in visited[1:]:
        if i == False:
            print("NO")
            break
    else:
        print("YES")


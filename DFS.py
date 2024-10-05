# --- DFS_traversal , none-recursive ,input : adjacancy matrix , list of nodes' name , start point(str)
                    
def DFS_traversal(G, nodes, start):
    visited = set()
    traversal_list = []
    start_index = nodes.index(start)
    stack = [start_index]
    while stack:
        node = stack.pop()
        
        
        if node not in visited:
            # Visit the node and add to traversal
            traversal_list.append(nodes[node])
            visited.add(node)
            
        
            # Find neighbors and push them to the stack
            for j in range(len(G)):
                if G[node][j] == 1 and j not in visited:
                    stack.append(j)
    
    return traversal_list

# A=[[0,1,1,1,0,0],
#    [1,0,0,0,1,0],
#    [1,0,0,0,0,1],
#    [1,0,0,0,0,1],
#    [0,1,0,0,0,0],
#    [0,0,1,1,0,0]]
# nodes=["a","b","c","d","e","f"]

# print(DFS_traversal(A,nodes,"a"))

#__________________________________________________________________________________________________________________

# --- DFS_traversal , none-recursive ,input : Graph:{"node":["adjacent node",...],...}  , start node          

def DFS_traversal_G(G, start):
    if start not in G:  # non-existent start node
        return []
    
    visited = set()
    stack = [start]
    traversal = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            traversal.append(node)
            visited.add(node)
            # Push unvisited neighbors to the stack
            stack.extend(neighbor for neighbor in reversed(G[node]) if neighbor not in visited)
    
    return traversal


# G={"a":["b","c","d"],
#    "b":["a","e"],
#    "c":["a","f"],
#    "d":["a","f"],
#    "e":["b"],
#    "f":["c","d"]
#    }

# print(DFS_traversal_G(G,"a"))
#__________________________________________________________________________________________________________________

# --- DFS_traversal , none-recursive ,input : edge_list:[("node","neighbor"),...]  , start node 
def DFS_traversal_edge(G,start):
    visited=set()
    stack=[start]
    traversal=[]
    
    while stack:
        node=stack.pop()
        if node not in visited:
            traversal.append(node)
            visited.add(node)
        
        for edge in G :
            if edge[0]==node  and  edge[1] not in visited :
                stack.append(edge[1])
            #-----For undirected graphs
            if edge[1]==node  and  edge[0] not in visited :
                stack.append(edge[0])
                
    return traversal

# G=[("a","b"),("a","c"),("a","d"),("b","e"),("c","f"),("d","f")]
# print(DFS_traversal_edge(G,"a"))  

#__________________________________________________________________________________________________________________
#------  convert the edge list into an adjacency list to speed up the traversal
# Convert edge_list to adjacency list

from collections import defaultdict

   
def build_adjacency_list(edge_list):
    adj_list = defaultdict(list)
    for edge in edge_list:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])  # For undirected graph, include reverse direction
    return adj_list

def DFS_traversal_edge_Adjacancy(G,start):
    new_G=build_adjacency_list(G)
    return DFS_traversal_G(new_G,start)
           
# G=[("a","b"),("a","c"),("a","d"),("b","e"),("c","f"),("d","f")]
# # Output differs from function DFS_traversal_G due to different ordering of node neighbors.
# print(DFS_traversal_edge_Adjacancy(G,"a"))                  
















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

                
              










# A=[[0,1,1,1,0,0],
#    [1,0,0,0,1,0],
#    [1,0,0,0,0,1],
#    [1,0,0,0,0,1],
#    [0,1,0,0,0,0],
#    [0,0,1,1,0,0]]
# nodes=["a","b","c","d","e","f"]

# print(DFS_traversal(A,nodes,"a"))

# G={"a":["b","c","d"],
#    "b":["a","e"],
#    "c":["a","f"],
#    "d":["a","f"],
#    "e":["b"],
#    "f":["c","d"]
#    }

# print(DFS_traversal_G(G,"a"))

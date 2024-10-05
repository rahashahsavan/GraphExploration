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
            
        
            # Find neighbors and push them to the stack
            for j in range(len(G)):
                if G[node][j] == 1 and j not in visited:
                    stack.append(j)
    
    return traversal_list

            
       
A=[[0,1,1,1,0,0],
   [1,0,0,0,1,0],
   [1,0,0,0,0,1],
   [1,0,0,0,0,1],
   [0,1,0,0,0,0],
   [0,0,1,1,0,0]]
nodes=["a","b","c","d","e","f"]

print(DFS_traversal(A,nodes,"a"))
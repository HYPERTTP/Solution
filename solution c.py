# Author - SHIVDEEP SINGH
# DATE - 26-05-2022

##############################################################################################################################

# This situation canbe modelled as a graph and thinking cities as the nodes of the graph and roads as the edges of the graph
# so the problem basically reduces to counting the number of connected components in an undirected graph assuming roads 
# connect both ways eg(a->b and b->a)

# In this example I am using DFS(Depth First Search) to find the number of connected Components
# Please Note the connnected components are the number of islands that we have to find
# The time Complexity of DFS O(nodes + edges) 


# the following graph is taken into consideration
# 0 1 2
# 3 4

# Here I am maintating a visited array(to check which nodes have been visited) and storing the graph in an adjacency list(2D dynamic array)

class Graph:
 
    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
 


    # THE DFS function with temp array visited array    
    # DFS uses Recursion
    def DFSUtil(self, temp, v, visited):
 
        # Mark the current vertex as visited
        visited[v] = True
 
        # Store the vertex to list
        temp.append(v)
 
        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
 
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp
 
    # Adding undirected Edges to the graph 
    # Roads connect both ways

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
 
    def connectedComponents(self):
        visited = []
        cc = []

        ## Setting all the visited values as false initially
        for i in range(self.V):
            visited.append(False)

        # If visited value is false do DFS(Depth First Search)    
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc
 
 
# Driver Code
if __name__ == "__main__":
 
    # Create a graph given in the above diagram
    # 5 vertices numbered from 0 to 4

    # graph has 5 nodes 0,1,2,3,4
    g = Graph(5)

    # Adding edges 1-0 2-3 and 3-4
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)

    # Calling the connected components function and getting return in cc
    cc = g.connectedComponents()

    print("the number of islands are")

    # returning the size of returned array
    print(len(cc))
 

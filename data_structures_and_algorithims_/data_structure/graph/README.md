# Graphs
A Graph in the data structure can be termed as a data structure consisting of data that is stored among many groups of edges(paths) and vertices (nodes), which are interconnected. Graph data structure (N, E) is structured with a collection of Nodes and Edges. Both nodes and vertices need to be finite . 
Graphs are awesome data structures that you use every day through Google Search, Google Maps, GPS, and social media. They are used to represent elements that share connections
## Challenge
create a grapth that represented as adjacency list and contains add node , add edge , get nodes , get_neighbors and size methods 
## Approach & Efficiency
Big O of time --> O(n^2) Big O of space --> O(n)
## API

- AddNode(): Adds a new node to the graph, Takes in the value of that node, Returns the added node.
- AddEdge(): Adds a new edge between two nodes in the graph, Include the ability to have a “weight”
- GetNodes(): Returns all of the nodes in the graph as a collection (set, list, or similar)
- GetNeighbors(): Returns a collection of edges connected to the given node, Takes in a given node, Include the weight of the connection in the returned collection
- Size(): Returns the total number of nodes in the graph.

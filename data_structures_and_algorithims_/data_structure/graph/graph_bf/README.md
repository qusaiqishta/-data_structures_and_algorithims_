# Challenge Summary
In a breadth first traversal, you are starting at a specific vertex/node. This node must be specified when calling the BreadthFirst() method. At first will visit each node connected to that node then will visit each node connected to that nodes(third level ) and so on..
## Whiteboard Process
![](/images/bfs_graph.png)
## Approach & Efficiency
Big O of time --> O(n^2) Big O of space --> O(n)

## Solution
```
def breadth_first_search(self,start_node):
        nodes=[]
        visited=set()
        breadth=Queue()   
        breadth.enqueue(start_node) 
        visited.add(start_node)
        while len(breadth):
            node=breadth.dequeue()
            nodes.append(node)
            
            for vertix in self.adjacency_list[node]:
                if vertix not in visited:
                    breadth.enqueue(vertix)
                    visited.add(vertix)
        return nodes           

```
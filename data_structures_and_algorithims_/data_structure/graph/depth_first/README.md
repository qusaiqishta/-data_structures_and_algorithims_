# Challenge Summary
Traverse through graph nodes using depth first approach
## Whiteboard Process
![](/images/depth_first_graph.png)
## Approach & Efficiency
Big O of time --> O(n^2) Big O of space --> O(n)
## Solution
```

    def depth_first_search(self, start_vertex):
            nodes = []
            visited = set()
            stack = Stack()

            stack.push(start_vertex)
            visited.add(start_vertex.value)

            while stack:
                current = stack.pop()
                nodes.append(current.value)
                neighbors = self.get_neighbors(current)

                for neighbor in neighbors:
                    if not neighbor in visited :
                        stack.push(neighbor.vertex)
                        visited.add(neighbor.vertex.value)


            if start_vertex not in self._adjacency_list:
                    return "Start node does not exist"

            return visited

```
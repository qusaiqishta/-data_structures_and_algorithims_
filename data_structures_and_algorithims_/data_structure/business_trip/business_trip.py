from collections import deque
class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value) 

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)
class Vertix:
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return f'Vertix > {self.value}'

class Edge:
    def __init__(self,vertix,weight):
        self.vertix=vertix
        self.weight=weight

class Graph:
    def __init__(self):
        self.adjacency_list={}

    def add_node(self,value):
        v=Vertix(value)
        self.adjacency_list[v]=[]
        return v   

    def add_edge(self,start_node,end_node,weight=0):
        if start_node not in self.adjacency_list:
            raise KeyError("start node not found")       
        if end_node not in self.adjacency_list:
            raise KeyError("end node not found")
        edge=Edge(end_node,weight)
        self.adjacency_list[start_node].append(edge)

    def get_nodes(self):
        return self.adjacency_list.keys()

    def get_neighbors(self, node):
            arr=[]
            if node in self.adjacency_list :
                for edge in self.adjacency_list[node]:
                    arr.append((edge.vertix, edge.weight))
                return arr

    
    def size(self):
        return len(self.adjacency_list)    

    
    def breadth_first_search(self,start_node):
        nodes=[]
        visited=set()
        breadth=Queue()   
        breadth.enqueue(start_node) 
        visited.add(start_node)
        while len(breadth):
            node=breadth.dequeue()
            nodes.append(node.value)
            
            for vertix in self.adjacency_list:
                if vertix not in visited:
                    breadth.enqueue(vertix)
                    visited.add(vertix)
        return nodes    

    def __str__(self):
        output = ''
        for vertix in self.adjacency_list.keys():
            # Concatenate the value of vertix
            output += vertix.value
            # Iterate over all edges of this vertix
            for edge in self.adjacency_list[vertix]:
                output += ' -> ' + edge.vertix.value 
            # Add a new line
            output += '\n'
        return output                                  

    
def business_trip(graph,cities):
    isdirect = True
    cost = 0
    for i in range(len(cities)-1):
        for city in graph.get_neighbors(cities[i]):
            if cities[i+1]==city[0]:
                cost+=city[1]
                break
            else:
                can=False
        
    if isdirect==False:
            cost=0
    
    return isdirect, f'${cost}'

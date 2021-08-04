# CAN'T IMPORT FOR SOME REASONS

from collections import deque

class Node:
    def __init__(self,value):
        self.value = value
        self.next=None

class  Stack:
    def __init__(self):
        self.top=None
        
    def push(self,value):
        node=Node(value)
        node.next=self.top
        self.top=node

    def pop(self):
        try:
            popped=self.top.value
            self.top=self.top.next # reassign the top to the next value
            return popped
        except:
            return 'Empty Stack'

    def peek(self):
        if self.top==None:
            raise Exception('empty list')

        return self.top.value

    def isEmpty(self):
        return self.top==None

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

    def get_neighbors(self,vertex):
        return self.adjacency_list.get(vertex,[])

    
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

#______________________________________________depthFirst________________________________________________________


    
    def depth_first_search(self, start_vertex):
            if start_vertex not in self.adjacency_list:
                    return "Start node does not exist"
            nodes = []
            visited = set()
            stack = Stack()

            stack.push(start_vertex)
            visited.add(start_vertex.value)

            while stack:
                current = stack.pop()
                nodes.append(current)
                neighbors = self.get_neighbors(current)

                for neighbor in neighbors:
                    if not neighbor in visited :
                        stack.push(neighbor.vertix)
                        visited.add(neighbor.vertix.value)

                return visited


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

#_________________________________TESTS__________________________________________________


def test_dfs():
    g = Graph()
    node1 = g.add_node('Pandora')
    node2 = g.add_node('Arendelle')
    node3 = g.add_node('Metroville')
    g.add_edge(node1, node2)
    g.add_edge(node2, node3)
    g.add_edge(node1, node3)
   
    assert g.depth_first_search(node1)=={'Arendelle', 'Metroville', 'Pandora'}


def test_dfs_2():
    graph = Graph()
    a = graph.add_node('a')
    c = graph.add_node('c')
    d = graph.add_node('d')
   
    graph.add_edge(a, c)
    graph.add_edge(a, d)
   
    graph.add_edge(c, a)
    
    graph.add_edge(d, a)
   
    assert graph.depth_first_search(a)=={'a', 'c', 'd'}


def test_depth_first_2():
    g = Graph()
    node1 = g.add_node('1')
    node2 = Vertix('2')
    assert g.depth_first_search(node2) == "Start node does not exist"    
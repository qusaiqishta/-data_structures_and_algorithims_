#   I CAN NOT IMPORT

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
                isdirect=False
        
    if isdirect==False:
            cost=0
    
    return isdirect, f'${cost}'



    

#_______________________________TESTS___________________________________________________________
def test_add_node():
    graph=Graph()
    assert  graph.add_node('a').value=='a'

def test_size_empty():
    graph=Graph()
    assert   graph.size()==0

def test_size():
    graph=Graph()
    graph.add_node('a')
    assert graph.size()==1

def test_get_nodes():
    g2 = Graph()
    node1 = g2.add_node('a')
    node2 = g2.add_node('b')
    node3 = g2.add_node('c')
    node4 = g2.add_node('d')

    g2.add_edge(node1,node3)
    g2.add_edge(node1,node4)
    g2.add_edge(node2,node3)
    nodes=g2.get_nodes()
    result=[]
    for node in nodes:
        result.append(node.value)
    assert result==['a', 'b', 'c', 'd']  

def test_get_nodes_empty():
    graph = Graph()
    assert len(graph.get_nodes()) == 0

def test_get_neighbors_node():
    graph = Graph()
    a = graph.add_node('a')
    c = graph.add_node('c')
    graph.add_edge(a, c)
    actual=graph.get_neighbors(a)[0][0]
    expected=c
    assert actual==expected


def test_no_neighbors():
    graph = Graph()
    a = graph.add_node('a')
    neighbors = graph.get_neighbors(a)
    assert len(neighbors) == 0
    assert neighbors == []


def test_add_edge():
    graph=Graph()
    start=graph.add_node('a')
    end=graph.add_node('b')
    graph.add_edge(start,end)
    expected=end
    actual = graph.get_neighbors(start)[0][0]
    assert actual==expected

def test_breadth_fisrt_graph():
    graph = Graph()
    node1 = graph.add_node('node1')
    node2 = graph.add_node('node2')
    node3 = graph.add_node('node3')
    graph.add_edge(node1,node2,node3)
    assert graph.breadth_first_search(node1) == ['node1','node2','node3']

def test_breadth_first():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(b, f)
    graph.add_edge(c, a)
    graph.add_edge(c, b)
    graph.add_edge(c, e)
    graph.add_edge(d, a)
    graph.add_edge(d, e)
    graph.add_edge(e, c)
    graph.add_edge(e, d)
    graph.add_edge(e, f)
    graph.add_edge(f, b)
    graph.add_edge(f, e)

    assert graph.breadth_first_search(a)==['a', 'b', 'c', 'd', 'e', 'f']


def test_business_trip():
    graph2 = Graph()

    pandora= graph2.add_node('pandora')
    arendelle= graph2.add_node('arendelle')
    metroville= graph2.add_node('metroville')
    narina= graph2.add_node('narina')
    naboo= graph2.add_node('naboo')
    manstropolis= graph2.add_node('manstropolis')

    graph2.add_edge(pandora,arendelle,150)
    graph2.add_edge(pandora,metroville,82)
    graph2.add_edge(arendelle,pandora,150)
    graph2.add_edge(arendelle,metroville,99)
    graph2.add_edge(arendelle,manstropolis,42)
    graph2.add_edge(metroville,pandora,82)
    graph2.add_edge(metroville,arendelle,99)
    graph2.add_edge(metroville,manstropolis,105)
    graph2.add_edge(metroville,naboo,26)
    graph2.add_edge(metroville,narina,37)
    graph2.add_edge(narina,metroville,37)
    graph2.add_edge(narina,naboo,250)
    graph2.add_edge(naboo,narina,250)
    graph2.add_edge(naboo,metroville,26)
    graph2.add_edge(naboo,manstropolis,73)
    graph2.add_edge(manstropolis,naboo,73)
    graph2.add_edge(manstropolis,arendelle,42)
    graph2.add_edge(manstropolis,metroville,105)
    assert business_trip(graph2,[metroville,pandora]) == (True, '$82')   
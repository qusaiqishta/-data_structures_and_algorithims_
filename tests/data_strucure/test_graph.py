#   I CAN NOT IMPORT
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



   
# CAN'T IMPORT FOR SOME REASONS
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


    def business_trip(self, cities):
        sum = 0
        flag = False
        for i in range(len(cities) - 1):
            neighbors = self.adjacency_list[cities[i]]

            for neighbor in neighbors:
                if cities[i + 1] == neighbor[i]:
                    sum+=neighbor[1]
                    flag = True
                    break
                else:
                    sum+=0
                    flag = False
        if not flag:
            return False, '$0'
        return True, '$' + str(sum)



if __name__=='__main__':
    graph = Graph()
    # Vertix_1 = graph.add_node('A')
    # Vertix_2 = graph.add_node('B')
    # Vertix_3 = graph.add_node('C')
    # Vertix_4 = graph.add_node('D')
    # Vertix_5 = graph.add_node('E')

    # graph.add_edge(Vertix_1, Vertix_2, 1)
    # graph.add_edge(Vertix_1, Vertix_3, 2)
    # graph.add_edge(Vertix_2, Vertix_4, 4)
    # graph.add_edge(Vertix_3, Vertix_4, 8)
    # graph.add_edge(Vertix_3, Vertix_5, 3)
    # graph.add_edge(Vertix_4, Vertix_5, 5)

    # assert graph.size() == 5

    # print(graph.get_nodes())
    # print(graph.get_neighbors(Vertix_1))
    # print(graph.get_neighbors(Vertix_2))
    # print(graph.get_neighbors(Vertix_3))
    # print(graph.get_neighbors(Vertix_4))
    # print(graph.get_neighbors(Vertix_5))
    # graph.print()
    g = Graph()
    node1 = g.add_node('Pandora')
    node2 = g.add_node('Arendelle')
    node3 = g.add_node('Metroville')
    node4 = g.add_node('Monstropolis')
    node5 = g.add_node('Narnia')
    node6 = g.add_node('Naboo')
    g.add_edge(node1, node2, 150)
    g.add_edge(node2, node3, 99)
    g.add_edge(node1, node3, 82)
    g.add_edge(node2, node4, 42)
    g.add_edge(node3, node4, 105)
    g.add_edge(node3, node5, 37)
    g.add_edge(node3, node6, 26)
    g.add_edge(node4, node6, 73)
    g.add_edge(node5, node6, 250)
    print(graph.business_trip([node1,node2]))
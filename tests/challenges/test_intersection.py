
class Node:
    def __init__(self,value):
        self.value = value
        self.left=None
        self.right=None

class Tree:
    
    def __init__(self):
         self.root=None

    def pre_order(self):

        output = ''
        if not self.root:
            return output

        # Define a closure function to be used internally
        def _traverse(node):
            nonlocal output # Because output is not accessible
            output = output + str(node.value) # Root

            if node.left:
                _traverse(node.left)

            if node.right:
                _traverse(node.right) 


            return output

        _traverse(self.root) 

        return output    

    

def tree_intersection(tree1,tree2):
    if not tree1.root:
        return"empty tree1"
    if not tree2.root:
        return"empty tree2"
            
    tree1=tree1.pre_order()
    tree2=tree2.pre_order()

    tree1_list=[]
    tree2_list=[]
    common=[]
    for char in tree1:
        tree1_list.append(char)
    for char in tree2:
        tree2_list.append(char)   
    for char in tree1_list:
        if char in tree2_list: 
            common.append(char)    
    return list(set(common))
#____________________tests________________________________________________________________________
def test_there_be_common():
    t1=Tree()
    t1.root=Node(1)
    t1.root.left=Node(2)
    t1.root.right=Node(3)
    
    t2=Tree()
    t2.root=Node(1)
    t2.root.left=Node(0)
    t2.root.right=Node(3)
    assert tree_intersection(t1,t2)==['1', '3']

def test_one_empty():
    t1=Tree()
    t2=Tree()
    t2.root=Node(1)
    t2.root.left=Node(0)
    t2.root.right=Node(3)
    assert tree_intersection(t1,t2)=='empty tree1'  

def test_two_empty():
    t1=Tree()
    t1.root=Node(1)
    t1.root.left=Node(2)
    t1.root.right=Node(3)
    
    t2=Tree()
    
    assert tree_intersection(t1,t2)=='empty tree2'

from data_structures_and_algorithims_.data_structure.trees.trees import Tree, Node ,BST 

import pytest




def test_pre_order(prepared_tree):
    assert prepared_tree.pre_order() == 'ABDECF'


def test_pre_order_empty_tree():
    tree = Tree()
    assert tree.pre_order() == ''

def test_in_order(prepared_tree):
    assert prepared_tree.in_order() == 'DBEAFC'   

def test_in_order_empty_tree():
    tree = Tree()
    assert tree.in_order() == ''

def test_post_order(prepared_tree):
    assert prepared_tree.post_order() == 'DEBFCA'    

def test_post_order_empty_tree():
    tree = Tree()
    assert tree.post_order() == ''

def test_BST_empty():
    tree=BST()
    assert tree.root==None  


def test_BST_add_value():
    tree=BST()
    tree.add(0)
    assert tree.root.value==0  

def test_BST_right_and_left():
    tree=BST()
    tree.add(7)
    tree.add(9)
    tree.add(3)
    assert tree.root.value==7
    assert tree.root.right.value==9
    assert tree.root.left.value==3


def test_BST_contains():
    tree=BST()
    tree.add(7)
    tree.add(9)
    tree.add(3)
    assert tree.contains(7)==True
    assert tree.contains(10)==False


def test_max_value(prepared_tree_num):
    assert prepared_tree_num.max_value()==10


def test_breadth(prepared_tree_breadth):    
    assert prepared_tree_breadth.breadth_first()==[1,2,3,4,5]

def test_breadth_empty():
    tree=Tree()    
    assert tree.breadth_first()==None
        




@pytest.fixture
def prepared_tree():
    tree = Tree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    return tree

@pytest.fixture
def prepared_tree_num():
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(-1)
    tree.root.left.left = Node(10)

    return tree    

@pytest.fixture
def prepared_tree_breadth():
    tree=Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right=Node(5)  

    return tree    
        
    
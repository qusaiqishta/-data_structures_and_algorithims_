from data_structures_and_algorithims_.data_structure.stacks_and_queues.stacks_and_queues import Queue
from data_structures_and_algorithims_.data_structure.trees.trees import Node , Tree

from data_structures_and_algorithims_.challenges.tree_fizz_buzz.tree_fizz_buzz import *


def test_fizz_buzz():
    b_tree = Tree()
    b_tree.root = Node(15)
    b_tree.root.left = Node(8)
    b_tree.root.right= Node(9)
   
    assert fizz_buzz_tree(b_tree) ==['FizzBuzz', '8', 'Fizz']
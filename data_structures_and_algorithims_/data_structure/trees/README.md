# Trees

A binary tree is a type of data structure for storing data such as numbers in an organized way. Binary search trees allow binary search for fast lookup, addition and removal of data items, and can be used to implement dynamic sets and lookup tables.


# Challenge 

Create a Binary Tree class

1- Define a method for each of the depth first traversals:
- pre order

- in order
   
- post order which returns an array of the values, ordered appropriately.

2- Create a Binary Search Tree class with the following methods:

- Add : Adds a new node with that value in the correct location in the binary search tree.

- Contains : Returns boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency

- Time: O(n)

- space: O(1)


# API 

- pre_order : Process all nodes of a tree by processing the root, then recursively processing all subtrees.

- in_order: Process all nodes of a tree by recursively processing the left subtree, then processing the root, and finally the right subtree

- post_order : Process all nodes of a tree by recursively processing all subtrees, then finally processing the root

- Add : Adds a new node with that value in the correct location in the binary search tree.

- Contains : Returns boolean indicating whether or not the value is in the tree at least once.

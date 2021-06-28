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


---

# Max_tree

##  Challenge Summary

write a method that return 
the maximum value in a tree




## Whiteboard Process

![](/images/max_tree.png)



## Approach & Efficiency

Big(O)->O(N)


## Solution 
```
tree=Tree()
    tree.root = Node(1)
    tree.root.left = Node(2000)
    tree.root.right = Node(-3)
    tree.max_value()
expected output=2000
_______________________________________

self.max=self.root.value=1
max_(node)

if node.right!=none   yess
max_(-3)

if self.max<node.right.value   NOO

if node.left!=none    yess
max_(2000)

if self.max<node.left.value    yess
self.max=self.left.value =200

return 2000
```


---

# breadth_first


## Challenge Summary

a function called breadth_first 
that return a  list of all values in the tree, in the order they were encountered


## Whiteboard Process

![](/images/breadth_first.png)


## Approach & Efficiency

Big(O)->O(N)

## Solution

```

input:  

 tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right=Node(5)  

expected output:
[1,2,3,4,5]

breadth=Queue()

self.root=1
result=[]
breadth.enqueu(1)
while 1
current=1
if 2
breadth.enqueu(2)

if 3:
breadth.enqueu(3)
result.append(1)
breadth.dequeue()
result=[1]
---------------------
next current=2
if 4
breadth.enqueu(4)
if 5
breadth.enqueu(5)

rsult.append(2)
breadth.dequeue()

result=[1,2]

.
.
.
so on

rsult=[1,2,3,4,5]


```
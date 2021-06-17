# Singly Linked List


Linked List can be defined as collection of objects called nodes that are randomly stored in the memory.

A node contains two fields i.e. data stored at that particular address and the pointer which contains the address of the next node in the memory. The last node of the list contains pointer to the null.




# challenge

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node. Within the LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.

# Efficiency


- insert : time : O(1) space : O(1)

- append : time : O(n) space : O(1)

- includes : time : O(n) space : O(1)

- __ str __ time : O(n) space : O(n)

- insertBefore : time : O(n) space : O(1)

- insertAfter : time : O(n) space : O(1)


# Whiteboard process

## append

![](/images/append.png)


## insertAfter

![](/images/insertAfter.png)



## inserBefore

![](/images/insertBefore.png)


## kth_from_end
![](/images/kth_from_end.png)



# API

insert

Add a new node to start of a list

includes

check if a specific node exist in a list or not

append

Takes any value as an argument and adds a new node with that value to the end of the list.

insertBefore

Add a new node with the given newValue immediately before the first value node

insertAfter

Add a new node with the given newValue immediately after the first value node

kthFromEnd

Takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list.




str
Takes in no arguments and returns a string representing all the values in the Linked List, formatted as:

{ a } -> { b } -> { c } -> NULL
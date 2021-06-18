## Stacks And Queues

Stacks and queues have a lot of things in common. They are both linear data structures in that you have one element and another element and then another element. They are both flexible with their sizes so you don't have to allocate initially them to have a size like 50, you can just add elements as you go and then also shrink it down. The main difference comes in how elements are removed from the stack or from the queue. A stack is what would be called a LIFO data structure, last in first out. It's much like an actual stack of plates. The last plate you put on top of that stack, that's going to be the first one you remove, its LIFO, last in first out. A queue though, is FIFO, first in first out. So think about a queue or line of people waiting to get into a movie theater. When the movie theater doors open they don't first serve the person who just hopped into line five seconds ago. They serve the person who got in line at the very very beginning an hour or two ago, and then the next person and then the next person. The very first person in is the very first person removed.



## Challenge

- Create a stack class that has push(To add in top of the stack) , pop(to remove from stack's top) , peek(to get the value in top) and isEmpty(to check is the stack is empty or not) methods

- Create a queue class that has enqueue(to add in rear of the queue) , dequeue(to remove from queue's front) , peek(to get the value in front) and is Empty methods


## Approach & Efficiency

Big(O)

- enqueue , dequeue , push  pop ,peek and isEmpty -> O(1)


## API

- Stack's methods

1- push :To add in top of the stack

2- pop :to remove from stack's top

3- peek :to get the value in top

4- isEmpty :to check is the stack is empty or not


- Queue's methods

1- enqueue :To add in rear of the queue

2- dequeue :to remove from queue's front

3- peek :to get the value in front

4- isEmpty :to check is the queue is empty or not

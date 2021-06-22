## Challenge summary

Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.


## Whiteboard process

![](/images/Animal-shelter.png)


## Approach & Efficiency

Big(o)-> O(N)linear 



## Solution

list:cat->cat->dog
list.enqueu_animals('cat')o enqueu
=>go the enqueue inside Queue class
and add 'cat' to be the new rear
list:cat->cat->cat->dog

dequeue_animals('cat')
self.rear not none and ='cat'

to_dequeue=self.front='dog'
to_dequeue.next=cat

while to_dequeue.next not none
to_dequeue=to_dequeue.next='cat'


removed =to_dequeue.next='cat'
to_dequeue.next=to_dequeue.next.next

return 'cat'

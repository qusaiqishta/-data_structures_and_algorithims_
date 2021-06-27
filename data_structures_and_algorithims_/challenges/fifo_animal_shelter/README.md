## Challenge summary

Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.


## Whiteboard process

![](/images/animal-shelter-fixed.png)


## Approach & Efficiency

Big(o)-> O(N)linear 



## Solution
```
list:cat->cat->dog
list.enqueue('cat')

new_animal='cat'
self.rear!=None

self.rear.next='cat'
self.rear='cat'
list:cat->cat->cat->dog
-----------------

list.dequeue(CAT)=='cat'

while current.next

if current.next.kind==kind  yess
temp=current.next='cat'
current.next=current.next.next='cat'

return 'cat'

list:cat->cat->dog

```
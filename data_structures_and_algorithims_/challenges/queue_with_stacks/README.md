# Challenge Summary

PseudoQueue class will internally only utilize to satck objects to do enqueue and dequeue methods


## Approach & Efficiency

Big(o)->O(1)


## WhiteBoard process
![](/images/queue-with-stack.png)






## Solution


```

list=PseudoQueue()

list.enqueu(0)
list.enqueu(1)
output: [0]->[1]

self.instack.push(0)

=>go to Stack class and use 
push method to insert 0 and 1
inside the list like this

def push(self,value):
        node=Node(value)
        node.next=self.top
        self.top=node

consedirng 1

node=NOde(1)
node.next=0
self.top=1 which means put 1 in 
front of 0


dequue()
while 1
self.outstack.push(0)
return 1

```
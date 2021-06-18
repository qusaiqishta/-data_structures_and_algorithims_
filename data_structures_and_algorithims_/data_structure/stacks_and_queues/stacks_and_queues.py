class Node:
    def __init__(self,value):
        self.value = value
        self.next=None

class  Stack:
    def __init__(self):
        self.top=None
        
    def push(self,value):
        node=Node(value)
        node.next=self.top
        self.top=node

    def pop(self):
        if self.top==None:
            raise Exception('empty list')    

       
        popped=self.top.value
        self.top=self.top.next # reassign the top to the next value
        return popped

    def peek(self):
        if self.top==None:
            raise Exception('empty list')

        return self.top.value

    def isEmpty(self):
        return self.top==None



class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        node=Node(value)
        if not self.rear: # if the queue is empty , make the value as front and rear 
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self):
        if self.front==None:
            raise Exception('empty queue')
        else:
            removed=self.front.value
            self.front=self.front.next
        return removed
        
    def peek(self):
        if self.front==None:
            raise Exception('empty queue')
        return self.front.value

    def isEmpty(self):
        return self.front==None



if __name__ == '__main__':
    list=Stack()
    print(list.isEmpty())

    list.push(0)
    list.push(1)
    list.push(2)
    list.pop()
    print(list.top)
   

    # list1=Queue()
    # list1.enqueue(0)
    # list1.enqueue(1)
    # print(list1.front.value)
    # list1.dequeue()
    # list1.dequeue()
    # print(list1.isEmpty())
 

    



            
           


            
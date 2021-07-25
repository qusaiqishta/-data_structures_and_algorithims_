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
        try:
            popped=self.top.value
            self.top=self.top.next # reassign the top to the next value
            return popped
        except:
            return 'Empty Stack'

    def peek(self):
        if self.top==None:
            self.isEmpty()
        else:    

            return self.top.value

    def isEmpty(self):
        return self.top==None


    def __str__(self):
        stack_str = ""
        if self.top:
            current = self.top
            while(current):
                stack_str += f"[{ current.value }] -> "
                current = current.next
        stack_str += "NULL"
        return (stack_str)    



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

    def __str__(self):
        queue_str = ""
        if self.front:
            current = self.front
            while(current):
                queue_str += f"[{ current.value }] -> "
                current = current.next
        queue_str += "NULL"
        return (queue_str)       



if __name__ == '__main__':
    list=Stack()
  

    list.push(1)
    list.push(2)
    list.push(3)
    
    print(list)
 
   

    # list1=Queue()
    # list1.enqueue(0)
    # list1.enqueue(1)
    # list1.enqueue(2)
    # print(str(list1))
    # # list1.dequeue()
    # # list1.dequeue()
    # # print(list1.isEmpty())
 

    



            
           


            
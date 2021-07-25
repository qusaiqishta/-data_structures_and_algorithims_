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
            return (popped)
        except:
            return 'Empty Stack'

    def peek(self):
        if self.top==None:
            raise Exception('empty list')

        return self.top.value

    def isEmpty(self):
        return self.top==None

    def __str__(self):
        output=''
        current=self.top
        while current:
            output+=f"[{current.value}]->" 
            current=current.next
        output+='NULL'
        return output       


class PseudoQueue:
    def __init__(self):
        self.inStack=Stack()
        self.outStack=Stack()

    def enqueue(self,value):
        self.inStack.push(value)

    def dequeue(self):
        if self.inStack.top==None and self.outStack.top==None:
            raise AttributeError('empty Queue')
        if self.outStack.top==None:
            while self.inStack.top:
                self.outStack.push(self.inStack.pop()) 
        return self.outStack.pop()                 


if __name__ == '__main__':
    list=PseudoQueue()
    list.enqueue(1)  
    list.enqueue(2) 
    list.enqueue(3)
    print(list.inStack.top.value)     
    



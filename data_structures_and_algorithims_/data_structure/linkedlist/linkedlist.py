
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head=None #start from empty list

    def insert(self,value): 

        new_node=Node(value)
        if self.head==None: # if there is no value as a head , make the new inserted on the head 
            self.head=new_node
        else:
            new_node.next=self.head 
            self.head=new_node

    def includes(self,value):
        current=self.head  # means start from the first element
        while current!=None:
            if current.value==value:
                return True

            else:
                current=current.next # means continue searching 
        return False 

    def deleteValue(self,value):
        if self.includes(value)==False:
            return " the value Does not exist"
        else:
            current=self.head
            if current.value==value:
                self.head=current.next
            else:
                while current.next.value!=value:
                    current=current.next
                current.next=current.next.next # skip the value that will be deleted    

   

    def append(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=node

           

    def insertBefor(self,value,newVal):
        if self.includes(value) == True:
            node= Node(newVal)
            if self.head.value == value:
                return self.insert(newVal)
            current=self.head
            while  current.next.value!= value:
                current = current.next
            node.next = current.next
            current.next=node


    def insertAfter(self,value,newVal):
        if (self.includes(value) == False):
            return('Value does not exist.')
        else:
            node = Node(newVal)
            current = self.head
            while(current.value != value):
                current = current.next
            node.next = current.next
            current.next = node


    def list_length(self):
        current=self.head
        length=0
        while (current):
            length+=1
            current=current.next
        return length


    def kth_from_end(self,k):
        list_length=self.list_length()
        if type(k)!=int or k<0:
            raise TypeError('You entered a non valid value , enter positive integer number')
        elif k>list_length-1:
            raise IndexError('index out of range')
        elif list_length==0:
            raise Exception('List is empty')    

        else:
            result=[]
            current=self.head

        while (current):
            result+=[current.value]
            current=current.next
            if current==None:
                break

        return result[::-1][k]

    def kth_from_end_no_extra_space(self,k):
        list_length=self.list_length()
        if type(k)!=int or k<0:
            raise TypeError('You entered a non valid value , enter positive integer number')
        elif k>list_length-1:
            raise IndexError('index out of range')
        elif list_length==0:
            raise Exception('List is empty')  

        else:
            value_index=list_length-1-k
            counter=0
            current=self.head
            while current:
                if counter==value_index:
                    return (current.value)
                counter+=1
                current=current.next    

    def delete_kth_from_end(self,k):
        list_length=self.list_length()
        if type(k)!=int or k<0:
            raise TypeError('You entered a non valid value , enter positive integer number')
        elif k>list_length-1:
            raise IndexError('index out of range')
        elif list_length==0:
            raise Exception('List is empty')  

        else:
            value_index=list_length-1-k
            counter=0
            current=self.head
            while current:
                if counter==value_index:
                    return self.deleteValue(current.value)
                counter+=1
                current=current.next

     





    # def __str__(self):
    #     values = []
    #     current = self.head
    #     while current:
    #         values.append(current.value)
    #         current = current.next
    #     return f'{values}'
   
    def __str__(self):
         if self.head!=None:
             list=''
             current=self.head
             while current:
                 list+=f'{{{current.value}}} ->'   
                 current=current.next
             list+='NULL'
             return list
         else:
            return 'It is an empty list !!!'   


if __name__ == '__main__':


    array2 = LinkedList()
    array = LinkedList()
    array.append(1)
    array.append(2)

    array.append(3)
    array.append(3)
    array.insertAfter(2,0)
    print(array)
    array.kth_from_end_no_extra_space(0)
    print(array)
    array2.insert(1)
    array2.insert(2)
    array2.insert(3)


    print(array2)

    

    

    
    

    
  

  
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
            current=self.head
            while current.next!=None: # while a list doesn't contain an only value 
                current=current.next # make a current value the one next to the head .. until current.next=none ,which mean the last elem
            current.next=new_node   

    def includes(self,value):
        current=self.head  # means start from the first element
        while current!=None:
            if current.value==value:
                return True

            else:
                current=current.next # means continue searching 
        return False 

   

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





def zipLists(list_one,list_two):
    if (list_one.head==None):
        return list_two

    elif list_two.head==None:
        return list_one   

    elif list_one.head==None and list_two.head==None:
        return 'It is an empty list !!!'   
    else:     
        current_one=list_one.head

        current_two=list_two.head

        

        while current_one.next:

            list_one.insertAfter(current_one.value,current_two.value)
            current_one=current_one.next.next
            current_two=current_two.next
            if current_one==None:
                break
 
        while current_two:
            list_one.append(current_two.value)
            current_two=current_two.next


    return list_one


                 


if __name__ == '__main__':


    array2 = LinkedList()
    array = LinkedList()
    array.append(1)
    array.append(2)

    array.append(3)
    array2.append(4)
    array2.append(5)
    array2.append(6)

    print(array)

    print(zipLists(array,array2))
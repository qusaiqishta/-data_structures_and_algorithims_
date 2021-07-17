class Node:
  def __init__(self,value):
    self.value=value
    self.next=None


class LinkedList:
  def __init__(self):
    self.head=None

  def append(self,value):
    node=Node(value)

    if self.head==None:
      self.head=node
    else:
      current=self.head

      while current.next!=None:
        current=current.next
      current.next=node

  def insert(self,value):
    node=Node(value)

    if self.head==None:
      self.head=node 

    else:
      node.next=self.head
      self.head=node

  def contains(self,value):
    if self.head==None:
      return "you are looking for a value inside an empty list!!" 
    else:
      current=self.head

      while current:
        if current.value==value:
          return True 
        else:
          current=current.next

      return False         

  def insertBefor(self,val,newVal):
    if self.contains(val)==True:
      node=Node(newVal)
      if self.head.value==val:
       return self.insert(val)
      else:
        current=self.head

        while current.next.value!=val:
          current=current.next

        node.next=current.next
        current.next=node

  def insertAfter(self,val,newval):
    if self.contains(val)==True:
      node=Node(newval)
      current=self.head
      # while current.next!=None:
      #   current=current.next
      # if current.value==val:
      #   return self.append(newval)

      # else:
      #   current=self.head

      while current.value!=val:
        current=current.next

      node.next=current.next
      current.next=node

  
  def list_length(self): 
    length=0
    current=self.head
    while current:
      length+=1
      current=current.next
    return length          

  def kth_from_end_O_of_N_complixity(self,k):
    length=self.list_length()

    if type(k) is not int and k<0:
      raise TypeError('please enter a valid value, which is positive integer number ')

    elif k>length-1:
      raise IndexError('you exceed the indeces range')

    elif length==0:
      raise Exception  ('empty list')

    else:

      output=[]
      current=self.head

      while current:
        output+=[current.value]
        current=current.next

      return output[::-1][k] 

     

  def kth_from_end_o_of_1_complixity(self,k): 

    length=self.list_length()

    if type(k) is not int and k<0:
      raise TypeError('please enter a valid value, which is positive integer number ')

    elif k>length-1:
      raise IndexError('you exceed the indeces range')

    elif length==0:
      raise Exception  ('empty list')

    else:
        counter=0
        value_index=length-1-k 
        current=self.head
        while current:
          if counter==value_index:
            return current.value
          counter+=1
          current=current.next  

  def reverseList(self):
    new_head=None
    current=self.head

    while current:
      next=current.next
      current.next=new_head
      new_head=current
      current=next
    self.head=new_head  


  
  def __str__(self):
    if self.head!=None:
        output=''
        current=self.head

        while current:
            output+=f"{{{current.value}}} ->"
            current=current.next

        output+='NULL'
        return output
    else:
      return " it is an empty list"    
        

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



if __name__=='__main__':
  list=LinkedList()
  list.append(1)
  list.append(2)
  list.append(3)
  print(list)
  list.reverseList()
  print(list)

  list1=LinkedList()

  list1.append(4)
  list1.append(5)
  list1.append(6)


  



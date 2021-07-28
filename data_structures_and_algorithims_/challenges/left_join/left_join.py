# could not import for some reasons 
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
    def append(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=node
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return f'{values}'
        
class HashTable:
    def __init__(self,size):
        self.size=size
        self.map=[None]*size

    def hash(self,key):
        sum_of_ascci=0
        for ch in key:
            ascci_of_ch=ord(ch)
            sum_of_ascci+=ascci_of_ch
        temp_value=sum_of_ascci*19
        hashed_key=temp_value%self.size
        return hashed_key

    def add(self,key,value):
        hashed_key=self.hash(key)

        if not self.map[hashed_key]:
            self.map[hashed_key]=LinkedList()
        self.map[hashed_key].insert((key,value)) 

    def get(self,key):

        index=self.hash(key)
        

        if  self.map[index]:    
            current=self.map[index].head
            while current:
                if current.value[0]==key:
                    return current.value[1]
                current=current.next   
        else:
            return None        
    
    
    def contains(self, key):
        index=self.hash(key)
        
        if self.map[index]:
            current=self.map[index].head
            while current:
                if current.value[0]==key:
                    return True
                else:    
                    current=current.next
        return False            
# ___________________________________________________________________________________________#        
def left_join(hash1,hash2):
    output=[]
    
    for item in hash1.map:
        if item:
            
            current = item.head 
            while current:
                output+=[[current.value[0],current.value[1]]]
                current=current.next
    print(output)          
    for item in output:
        # print(item)
        if hash2.contains(item[0])==True:
            
            item.append(hash2.get(item[0]))
        else:
            item.append(None)
    return f"{output},"    

if __name__ == '__main__':
    h1 = HashTable(1024)
    h1.add('fond','enamored')        
    h1.add('wrath', 'anger')          
    h1.add('diligent', 'employed')    
    h1.add('outfit', 'garb')           
    h1.add('guide', 'usher')

    h2 = HashTable(1024)
    h2.add('fond', 'averse')
    h2.add('wrath', 'delight')
    h2.add('diligent', 'idle')
    h2.add('guide', 'follow')
    h2.add('flow]', 'jam')


    print(left_join(h1,h2))     

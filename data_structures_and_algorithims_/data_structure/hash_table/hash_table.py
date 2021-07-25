
from data_structures_and_algorithims_.data_structure.linkedlist.linkedlist import Node, LinkedList



class HashTable:
    def __init__(self,size):
<<<<<<< HEAD

=======
>>>>>>> 82c4a39ec20e4c5c83290074d8af81992c468636
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
<<<<<<< HEAD
        index=self.hash(key)
        print('this is index: ' ,index)
=======

        index=self.hash(key)
>>>>>>> 82c4a39ec20e4c5c83290074d8af81992c468636
        print('________from get')

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
        print('________from contains')
        if self.map[index]:
            current=self.map[index].head
            while current:
                if current.value[0]==key:
                    return True
                else:    
                    current=current.next
        return False            

                 



if  __name__ == '__main__':
    
    hashTable=HashTable(100)
    # hashTable.add('avanti','112hp')
<<<<<<< HEAD
    hashTable.add('crv','216hp')
    hashTable.add('silent', True)
=======
    # hashTable.add('crv','216hp')
    # hashTable.add('silent', True)
>>>>>>> 82c4a39ec20e4c5c83290074d8af81992c468636
    hashTable.add('listen', 'Hey man')
    # hashTable.hash('listen')
    print(hashTable.get('listen'))
    
    print(hashTable.contains('listen'))
    
    for item , index in enumerate(hashTable.map):
        if item:
            print(index,item)                    







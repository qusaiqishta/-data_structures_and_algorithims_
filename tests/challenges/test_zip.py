from data_structures_and_algorithims_.data_structure.linkedlist.linkedlist import LinkedList 
from data_structures_and_algorithims_.challenges.ll_zip.ll_zip import zipLists





def test_zip_1st_empty():
    list1 = LinkedList()
    list2 = LinkedList()
    list2.append(1)
    list2.append(2)
    list2.append(3)
    
    
    assert str(zipLists(list1,list2))=="{1} ->{2} ->{3} ->NULL"

def test_zip_2nd_empty():
    list1=LinkedList()
    list2=LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)

    assert str(zipLists(list1,list2))== "{1} ->{2} ->{3} ->NULL" 

def test_zip_two_are_empty():
    list1=LinkedList()
    list2=LinkedList()

    assert str(zipLists(list1,list2))=='It is an empty list !!!'    


def test_zip_same_length():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list2.append(4)
    list2.append(5)
    list2.append(6)
    
    
    
    assert str(zipLists(list1,list2))=='{1} ->{4} ->{2} ->{5} ->{3} ->{6} ->NULL' 


def test_zip_two_has_bigger_length():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.append(1)
    list1.append(2)
    
    list2.append(4)
    list2.append(5)
    list2.append(6)
    
    
    assert str(zipLists(list1,list2))=="{1} ->{4} ->{2} ->{5} ->{6} ->NULL"   


def test_zip_one_has_bigger_length():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list2.append(4)
    list2.append(5)
    
    assert str(zipLists(list1,list2))=="{1} ->{4} ->{2} ->{5} ->{3} ->NULL"
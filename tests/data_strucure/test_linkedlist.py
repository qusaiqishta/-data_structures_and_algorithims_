
 
from data_structures_and_algorithims_.data_structure.linkedlist.linkedlist  import LinkedList 


import pytest


# @pytest.mark.skip
def test_insert_1():
    ll1 = LinkedList()
    ll1.insert(1)
    actual = ll1.__str__()
    expected='{1} ->NULL'
    assert actual==expected

def test_head_value():
    ll = LinkedList()
    ll.insert(0)
    actual=ll.head.value
    expected=0
    assert actual==expected    


# @pytest.mark.skip
def test_insert_output():
    ll = LinkedList()
    ll.insert(1)
    ll.insert('qa')
    actual = ll.__str__()
    expected='{qa} ->{1} ->NULL'
    assert actual==expected    


def test_includes_True():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    actual = ll.includes(1)
    expected=True
    assert actual==expected  

def test_includes_False():
    # Will return false when searching for a value in the linked list that does not exist
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    actual = ll.includes(4)
    expected=False
    assert actual==expected      




def test_append_1():
    ll1 = LinkedList()
    ll1.append(1)
    assert ll1.head.value==1 

def test_append(): 
    list=LinkedList()
    list.append(1)
    list.append(3)
    list.append(5) 
    assert list.head.value==1
    assert list.head.next.value==3
    assert list.head.next.next.value==5 

def test_insert_before():
    list=LinkedList()
    list.append(1)
    list.append(3)
    list.append(5) 
    list.insertBefor(3,10)
    assert list.head.next.value==10


def test_insert_before_head():
    list=LinkedList()
    list.append(1)
    list.append(3)
    list.append(5) 
    list.insertBefor(1,10)
    assert list.head.next.value==1    

def test_insert_after_head():
    list=LinkedList()
    list.append(1)
    list.append(3)
    list.append(5) 
    list.insertAfter(1,10)
    assert list.head.next.value==10


def test_insert_after():
    list=LinkedList()
    list.append(1)
    list.append(3)
    list.append(5) 
    list.insertAfter(3,10)
    assert list.head.next.next.value==10    

def test_kth_from_end_k_greater_than_length():
    with pytest.raises(Exception):
        assert input_list.kth_from_end(10)

def test_kth_from_end_k_less_than_zero():
    with pytest.raises(Exception):
        assert input_list.kth_from_end(-10)=='You entered a non valid value , enter positive integer number'        


def test_kth_from_end_k_empty_list():
    with pytest.raises(Exception):
        assert input_list_empty.kth_from_end(0)=='List is empty'



def test_kth_from_end_k():
    with pytest.raises(Exception):
        assert input_list_empty.kth_from_end(0)==1


def test_kth_from_end_k():
    with pytest.raises(Exception):
        assert input_list_empty.kth_from_end(4)==5



@pytest.fixture
def input_list():
    list=LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    list.insert(4)
    list.insert(5)
    return list

def input_list_empty():
    list=LinkedList()
    return list    
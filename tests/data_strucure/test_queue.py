from data_structures_and_algorithims_.data_structure.stacks_and_queues.stacks_and_queues import Queue , Stack
import pytest
import unittest
def test_stack_push():   
    list=Stack()
    list.push(0)
    assert list.top==0


def test_stack_push_multiple():
    list=Stack()
    list.push(0)
    list.push(1)
    list.push(3)
    assert list.top==3

@pytest.mark.skip
def test_stack_pop():
    list=Stack()
    list.push(0)
    list.push(1)
    list.push(3)
    list.pop()
    assert list.top==1

@pytest.mark.skip
def test_stack_pop_empty():
    list=Stack()
    list.push(0)
    list.push(1)
    list.pop()
    list.pop()
    assert list.isEmpty()==False   

@pytest.mark.skip
def test_stack_peek():
    list=Stack()
    list.push(0)
    list.push(-1)
    assert list.peek()==-1

def test_enqueue():
    list=Queue()
    list.enqueue(0)
    assert list.rear.value==0 


def test_enqueue_multiple():
    list=Queue()
    list.enqueue(0)
    list.enqueue(1)
    list.enqueue(2)
    assert list.rear.value==2 
    assert list.front.value==0  


def test_dequeue():
    list=Queue()
    list.enqueue(0)
    list.enqueue(1)
    list.enqueue(2)
    list.dequeue()
    assert list.rear.value==2  
    assert list.front.value==1

def test_queue_peek():
    list=Queue()
    list.enqueue(0)
    list.enqueue(1)
    list.enqueue(2)
    assert list.peek()==0

def test_queue_isEmpty_true():
    list=Queue()
    list.enqueue(1)
    list.enqueue(2)
    list.dequeue()
    list.dequeue()
    assert list.isEmpty()==True     


def test_queue_isEmpty_false():
    list=Queue()
    list.enqueue(0)
    assert list.isEmpty()==False 

def test_queue_instantiate():  
    list=Queue()
    assert  list.front==None  
    assert  list.rear==None   

def test_queue_throws_exception():
    list=Queue()
    with pytest.raises(Exception):
        assert list.dequeue()
        assert list.peek()

                               



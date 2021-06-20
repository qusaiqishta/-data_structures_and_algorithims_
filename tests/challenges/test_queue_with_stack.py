from data_structures_and_algorithims_.challenges.queue_with_stacks.queue_with_stacks import PseudoQueue
import pytest


def test_stack_enqueue():
    list=PseudoQueue()
    list.enqueue(0)
    assert list.inStack.top.value==0


def test_stack_enqueue_multible():
    list=PseudoQueue()
    list.enqueue(0)
    list.enqueue(1)
    list.enqueue(2)
    assert list.inStack.top.value==2

def test_stack_dequeue():
    list=PseudoQueue()
    list.enqueue(0)
    list.enqueue(1)
    list.enqueue(2)
    list.dequeue()
    assert list.outStack.top.value==1


def test_stack_dequeue_multiple():
    list=PseudoQueue()
    list.enqueue(0)
    list.enqueue(1)
    list.enqueue(2)
    list.dequeue()
    list.dequeue()
    assert list.outStack.top.value==2 

def test_stack_enqueue_empty_queue():
    list=PseudoQueue()
    with pytest.raises(AttributeError):
        assert list.dequeue()      





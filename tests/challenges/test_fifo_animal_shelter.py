from data_structures_and_algorithims_.challenges.fifo_animal_shelter.fifo_animal_shelter import *
from data_structures_and_algorithims_.data_structure.stacks_and_queues.stacks_and_queues import Queue , Node , Stack






def test_new_shelter():
    shelter = AnimalShelter()
    assert shelter.front == None
    assert shelter.rear == None 


def test_enqueu_shelter():
    shelter=AnimalShelter()
    shelter.enqueue_animals(Cat('cat1'))
    shelter.enqueue_animals(Cat('cat2'))
    shelter.enqueue_animals(Dog('dog1'))
    

    assert str(shelter)=='[cat1] -> [cat2] -> [dog1] -> NULL'


def test_dequeu_shelter():
    shelter=AnimalShelter()
    shelter.enqueue_animals(Cat('cat1'))
    shelter.enqueue_animals(Cat('cat2'))
    shelter.enqueue_animals(Dog('dog1'))
    shelter.dequeue_animals('Dog')
    

    assert str(shelter)=='[cat2] -> [dog1] -> NULL' 



def test_dequeu_shelter_specific():
    shelter=AnimalShelter()
    shelter.enqueue_animals(Cat('cat1'))
    shelter.enqueue_animals(Cat('cat2'))
    shelter.enqueue_animals(Dog('dog1'))
    shelter.dequeue_animals('Cat')
    shelter.dequeue_animals('Dog')
    
    

    assert str(shelter)=='[dog1] -> NULL'     

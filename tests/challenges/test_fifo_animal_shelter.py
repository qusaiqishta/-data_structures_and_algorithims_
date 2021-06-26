from data_structures_and_algorithims_.challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter
from data_structures_and_algorithims_.data_structure.stacks_and_queues.stacks_and_queues import Queue , Node , Stack






def test_new_shelter():
    shelter = AnimalShelter()
    assert shelter.front == None
    assert shelter.rear == None 

def test_enqueue_animal_shelter():
    shelter = AnimalShelter()
    shelter.enqueue_animals('cat')
    assert shelter.front.value == 'cat'

def test_enqueue_multiple_animal_shelter():
    shelter = AnimalShelter()
    shelter.enqueue_animals('cat')
    shelter.enqueue_animals('dog')
    assert shelter.front.value == 'cat'
    assert shelter.rear.value=='dog'

# def test_enqueue_animal_not_allowd():
#     shelter=AnimalShelter()
#     shelter.enqueue_animals('mouse')
#     assert shelter.front.value==None   
# 

def test_dequeue_animal_shelter():
    shelter = AnimalShelter()
    shelter.enqueue_animals('cat')
    shelter.enqueue_animals('dog')
    shelter.dequeue_animals('dog')
    assert removed =='dog'


def test_dequeue_animal_shelter_empty():
    shelter = AnimalShelter()
    shelter.dequeue_animals('dog')
    assert removed ==None   


from typing import Counter
from data_structures_and_algorithims_.data_structure.stacks_and_queues.stacks_and_queues import Queue , Node , Stack



class Dog:
    def __init__(self,value):
        self.value = value
        self.kind='dog'
        self.next=None

class Cat:
    def __init__(self,value):
        self.value = value
        self.kind='cat'
        self.next=None        


class AnimalShelter:
    def __init__(self):
        self.front=None
        self.rear=None


    def enqueue_animals(self, animal):
        new_animal=animal

        if not self.rear:
            self.rear=new_animal
            self.front=new_animal
        else:    
            self.rear.next=new_animal
            self.rear=new_animal    

    def dequeue_animals(self,kind=None):
        if not (kind=='dog') and not (kind=='cat'):
            temp=self.front
            self.front=self.front.next
            return temp.value

        else:
            current=self.front
            if self.front.kind==kind:
                temp=self.front
                self.front=self.front.next
                return temp.value
            else:
                while current.next:
                    if current.next.kind==kind:
                        temp=current.next
                        current.next=current.next.next
                        return temp.value

                    else:
                        current=current.next
                return None         

    def __str__(self):
        queue_str = ""
        if self.front:
            current = self.front
            while(current):
                queue_str += f"[{ current.value }] -> "
                current = current.next
        queue_str += "NULL"
        return (queue_str)                   

                               

        

if __name__ == '__main__':
    shelter =AnimalShelter()
    shelter.enqueue_animals(Cat('test'))
    shelter.enqueue_animals(Dog('test1'))
    shelter.enqueue_animals(Cat('test2'))
    print(shelter)
    shelter.enqueue_animals(Dog('dog'))
    print(str(shelter.dequeue_animals('dog')))
    print(shelter.dequeue_animals('bird'))
    
    print(shelter)
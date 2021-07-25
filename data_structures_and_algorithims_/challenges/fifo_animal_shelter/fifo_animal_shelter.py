from typing import Counter
from data_structures_and_algorithims_.data_structure.stacks_and_queues.stacks_and_queues import Queue , Node , Stack

class Cat:
    def __init__(self,name):
        self.name = name
        self.kind='cat'
       

class Dog:
    def __init__(self,name):
        self.name=name
        self.kind='dog'

class Animal:
    def __init__(self,name,kind):
        self.name = name
        self.kind = kind
        


class AnimalShelter:
   def __init__(self):
       self.cat=Queue()
       self.dog=Queue()

   def enqueue(self,animal):
        if  animal =='cat':
            self.cat.enqueue(animal)
        elif animal =='dog':
            self.dog.enqueue(animal)
        else:
            return " the animal should be either dog or cat"
   def dequeue(self,pref=None):
        if pref=='cat':
            self.cat.dequeue().name 
        elif pref=='dog':
            self.dog.dequeue().name    
        else:
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
    dj = Dog('dj')
    boby=Dog('boby')
    mert=Dog('mert')
    snow = Cat('snow')
    amy=Cat('amy')
    mshmsh=Cat('mshmsh')
    hmed=Animal('hmed','hores')
    animalShelter=AnimalShelter()
    animalShelter.enqueue(dj)
    animalShelter.enqueue(boby)
    animalShelter.enqueue(mert)
    animalShelter.enqueue(snow)
    animalShelter.enqueue(amy)
    animalShelter.enqueue(mshmsh)
    # print(animalShelter.enqueue(hmed))
    # print(animalShelter.dequeue('cat'))
    print(animalShelter)
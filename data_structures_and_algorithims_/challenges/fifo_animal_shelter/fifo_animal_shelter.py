from data_structures_and_algorithims_.data_structure.stacks_and_queues.stacks_and_queues import Queue , Node , Stack



class AnimalShelter(Queue):
    def __init__(self):
        self.front=None
        self.rear=None


    def enqueue_animals(self, animal):
        if animal=='dog' or animal=='cat':
            self.enqueue(animal)
        else:
            return None

    def dequeue_animals(self,pref):
        if self.rear is None:
            return None

        if pref=='dog' or pref=='cat':
            to_dequeue=self.front

            while(to_dequeue.next is not None and to_dequeue.next.value!=pref):
                to_dequeue=to_dequeue.next

            if to_dequeue.next==None:
                return None

            else: 
                removed = to_dequeue.next
                to_dequeue.next = to_dequeue.next.next
                return removed.value   
        else:
            return None        

if __name__ == '__main__':
    shelter=AnimalShelter()
    shelter.enqueue_animals('cat')
    shelter.enqueue_animals('dog')
    print(shelter.dequeue_animals('cat'))

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.num_items = 0
        self.front = None  # Front of the queue
        self.rear = None  # Back of the queue


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == 0:  # Nothing in the queue
            return True
        return False


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == self.capacity:  # queue is full
            return True
        return False

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.num_items == self.capacity:  # queue is full
            raise IndexError
        n_rear = Node(item)
        if self.front is None:  # If the queue is empty
            self.rear = n_rear
            self.front = n_rear
        else:  # if the queue is not empty
            self.rear.next = n_rear
            self.rear = n_rear
        self.num_items += 1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.num_items == 0:  # if the queue is empty
            raise IndexError
        dq = self.front.item
        if self.front.next is None:  # if the queue becomes empty after dequeuing
            self.rear = None
            self.front = None
            self.num_items -= 1
            return dq

        else:
            self.front = self.front.next
            self.num_items -= 1
            return dq





    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items

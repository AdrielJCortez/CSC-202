class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0
        self.front = None
        self.rear = None


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == 0:  # Nothing in the queue
            return True
        return False


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == self.capacity:  # Nothing in the queue
            return True
        return False

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.num_items == self.capacity:  # if the queue is full
            raise IndexError
        else:
            # Increment self.rear to point to the next available position
            if self.num_items == 0:
                self.items[0] = item
                self.front = 0
                self.rear = 0
                self.num_items = self.num_items + 1
            elif self.rear == self.capacity - 1:
                self.items[0] = item
                self.rear = 0
                self.num_items += 1
            else:
                self.items[self.rear + 1] = item
                self.rear += 1
                self.num_items += 1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.num_items == 0:  # if the queue is empty
            raise IndexError
        else:
            if self.front == self.capacity - 1:
                dq = self.items[self.front]
                self.front = 0
                self.num_items -= 1
            else:
                dq = self.items[self.front]
                self.front += 1
                self.num_items -= 1
        return dq


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items

class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.capacity = capacity
        self.heap_list = [None] * (capacity + 1)
        self.next_ava_idx = 1  # this is referencing the next available spot in our heap
        self.size = 0  # or the length of the list

    def perc_up(self, idx):
        item = self.heap_list[idx]  # finds the current item we are working with (perc up)
        parent = self.heap_list[idx // 2]  # finds the parent

        if parent is None:
            self.next_ava_idx += 1
            self.size += 1
            return True

        elif item > parent:  # checks if the item is greater than its parent then swaps if true
            self.heap_list[idx] = parent  # becomes the child
            self.heap_list[idx // 2] = item  # becomes the parent
            return self.perc_up(idx // 2)

        else:  # no switches available just puts the item as a child
            self.heap_list[idx] = item
            self.next_ava_idx += 1
            self.size += 1
            return True

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        # Should call perc_up
        if self.is_full():
            return False
        elif self.size == 0:
            self.heap_list[1] = item
            self.next_ava_idx += 1
            self.size += 1
        else:
            self.heap_list[self.next_ava_idx] = item
            return self.perc_up(self.next_ava_idx)

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.size == 0:
            return None
        return self.heap_list[1]

    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        if i * 2 >= self.capacity or self.heap_list[i * 2] is None:  # makes sures that it won't be compared to
            # something out of range or None
            return None

        elif (i * 2 + 1 >= self.capacity or self.heap_list[i * 2 + 1] is None) and self.heap_list[(i * 2)] is not None:
            # if there is only one child which is the left child
            left = self.heap_list[i * 2]  # left child
            item = self.heap_list[i]  # current item
            if left > item:
                self.heap_list[i] = left  # becomes parent
                self.heap_list[i * 2] = item  # becomes child
                return self.perc_down(i * 2)
            else:
                return None

        elif self.heap_list[(i * 2) + 1] is not None and self.heap_list[i * 2] is not None:
            left = self.heap_list[i * 2]  # left child
            right = self.heap_list[i * 2 + 1]  # right child
            item = self.heap_list[i]  # current item

            if left > right:  # left has higher priority
                if left > item:
                    self.heap_list[i] = left  # becomes parent
                    self.heap_list[i * 2] = item  # becomes child
                    return self.perc_down(i * 2)
                else:
                    return None
            elif right > left:  # right has higher priority
                if right > item:
                    self.heap_list[i] = right
                    self.heap_list[i * 2 + 1] = item
                    return self.perc_down(i * 2 + 1)
                else:
                    return None

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        # Should call perc_down
        if self.is_empty():  # if it's empty return None
            return None
        else:
            return_item = self.heap_list[1]  # item we are returning
            self.heap_list[1] = self.heap_list[self.size]  # item that will percolate
            self.heap_list[self.size] = None
            self.perc_down(1)
            self.size -= 1
            self.next_ava_idx -= 1
            return return_item

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        contents = []
        for num in self.heap_list:
            if num is not None:
                contents.append(num)
        return contents

    def build_heap_h(self, curr_par):
        if curr_par < 1:  # base case if my var is less than 2 then there will be no more parents
            return None
        self.perc_down(curr_par)  # perc down the parent
        return self.build_heap_h(curr_par - 1)

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in a list using the bottom-up construction method.
        If the capacity of the current heap is less than the number of 
        items in a list, the capacity of the heap will be increased to accommodate
        exactly the number of items in alist'''
        # Bottom-Up construction.  Do NOT call enqueue
        if self.capacity <= len(alist):
            self.heap_list = (len(alist) + 1) * [None]  # clears the current heap and will fit the next heap size
            self.capacity = len(alist) + 1
        else:
            self.heap_list = (self.capacity + 1) * [None]  # clears the current heap
        self.size = 0
        self.next_ava_idx = 1
        counter = 1
        for num in alist:  # puts all the items in the array in any order
            self.heap_list[counter] = num
            counter += 1
            self.next_ava_idx += 1
            self.size += 1
        return self.build_heap_h(len(alist) // 2)

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.heap_list[1] is None

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.heap_list[-1] is not None

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)

        for i in range(len(alist) - 1, -1, -1):
            alist[i] = self.dequeue()




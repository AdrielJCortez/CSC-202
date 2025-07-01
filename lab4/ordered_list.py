class Node:
    '''Node for use with doubly-linked list'''

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        dummy_node = Node(None)
        self.head = dummy_node
        dummy_node.next = dummy_node
        dummy_node.prev = dummy_node

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.head.next == self.head and self.head.prev == self.head

    def add_h(self, node, n_node) -> bool:
        if node == self.head:  # checks that the list has looped all the way around and the n_node is the largest int
            # or that its empty
            n_node.prev = self.head.prev
            n_node.next = self.head
            self.head.prev.next = n_node
            self.head.prev = n_node
            return True
        elif node.item == n_node.item:
            return False
        elif n_node.item < node.item:  # if the new node item is less than the current node item
            n_node.prev = node.prev
            n_node.next = node
            node.prev.next = n_node
            node.prev = n_node
            return True
        else:
            return self.add_h(node.next, n_node)

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head end of list) to highest (at tail end of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance.  Assume that all items added to your 
           list can be compared using the < operator and can be compared for equality/inequality.
           Make no other assumptions about the items in your list'''
        n_node = Node(item)
        return self.add_h(self.head.next, n_node)

    def remove_h(self, node, item):
        if node == self.head:  # Not found went all the way back to the dummy variable
            return False
        elif node.item == item:
            node.prev.next = node.next
            node.next.prev = node.prev
            return True
        else:
            return self.remove_h(node.next, item)

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
           returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        return self.remove_h(self.head.next, item)

    def index_h(self, node, item, idx_pos):
        if node == self.head:
            return None
        elif node.item == item:
            return idx_pos
        else:
            return self.index_h(node.next, item, idx_pos + 1)

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        return self.index_h(self.head.next, item, 0)

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        counter = 0
        current_node = self.head.next
        while counter <= index and current_node != self.head:
            if counter == index:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                return current_node.item
            current_node = current_node.next
            counter += 1
        raise IndexError

    def search_h(self, node, item):
        if node == self.head:
            return False
        elif node.item == item:
            return True
        else:
            return self.search_h(node.next, item)

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.search_h(self.head.next, item)

    def python_list_h(self, node, output):
        if node == self.head:
            return output
        else:
            return self.python_list_h(node.next, output + [node.item])

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        return self.python_list_h(self.head.next, [])

    def python_list_rev_h(self, node, output):
        if node == self.head:
            return output
        else:
            return self.python_list_rev_h(node.prev, output + [node.item])

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.python_list_rev_h(self.head.prev, [])

    def size_h(self, node):
        if node == self.head:
            return 0
        else:
            return 1 + self.size_h(node.next)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_h(self.head.next)

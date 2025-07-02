import math


class HashTable:

    def __init__(self, table_size):  # add appropriate attributes, NO default size
        ''' Initializes an empty hash table with a size that is the smallest
            prime number that is >= table_size (i.e. if 10 is passed, 11 will 
            be used, if 11 is passed, 11 will be used.)'''
        if not self.isPrime(table_size):
            table_size = self.next_prime(table_size)
        self.table_size = table_size
        self.hash = [None] * table_size
        self.num_items = 0

    # Function that returns True if n
    # is prime else returns False
    def isPrime(self, n):
        # Corner cases
        if n <= 1:
            return False
        if n <= 3:
            return True

        # This is checked so that we can skip
        # middle five numbers in below loop
        if n % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(n) + 1), 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False

        return True

    # Function to return the smallest
    # prime number greater than N
    def next_prime(self, N):
        if N <= 1:
            return 2

        prime = N + 1
        while True:
            if self.isPrime(prime):
                return prime
            prime += 1

    def rehash(self):
        curr_hash = self.hash  # a temp variable
        self.table_size = self.next_prime(self.table_size * 2)  # find the next prime after doubling the size
        self.hash = self.table_size * [None]  # new hash table
        self.num_items = 0  # we need to set this back to zero because when you insert it will add another 1
        for curr in curr_hash:
            if curr is not None:
                self.insert(curr[0], curr[1])  # insert each key into the new hash

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value can be anything (Object, None, list, etc.).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased
        to the next prime greater than 2*table_size.'''
        index = self.horner_hash(key) % self.table_size
        start = index
        tup = (key, value)

        i = 0
        while self.hash[index] is not None:
            if self.hash[index][0] == key:  # check if key has to update its value
                self.hash[index] = tup  # update the key-value pair
                return
            i += 1
            index = (start + (i ** 2)) % self.table_size  # otherwise update its index to try to find an open spot or
            # find that the key has to update
        self.hash[index] = tup  # enter as a new value if it skips the while loop condition
        self.num_items += 1

        if self.get_load_factor() > 0.5:
            self.rehash()

    def horner_hash(self, key):
        ''' Compute the hash value by using Horner’s rule, as described in project specification.
            This method should not mod with the table size'''
        n = min(8, len(key))
        hash_value = 0
        for i in range(n):
            hash_value += (ord(key[i]) * 31 ** (n - 1 - i))
        return hash_value

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        index = self.horner_hash(key) % self.table_size
        start = index
        i = 0
        while self.hash[index] is not None:  # checks if its none
            if self.hash[index][0] == key:
                return True
            else:
                i += 1
                index = (start + (i ** 2)) % self.table_size
        return False  # this means it skipped the while loop condition (which is None)

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        index = self.horner_hash(key) % self.table_size
        start = index
        i = 0
        while self.hash[index] is not None:
            if self.hash[index][0] == key:
                return index
            else:
                i += 1
                index = (start + (i ** 2)) % self.table_size
        return None


    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        keys = []
        for i in range(self.table_size):
            if self.hash[i] is not None:
                word = self.hash[i][0]
                keys.append(word)
        return keys

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        index = self.horner_hash(key) % self.table_size
        start = index
        i = 0
        while self.hash[index] is not None:
            if self.hash[index][0] == key:
                return self.hash[index][1]
            else:
                i += 1
                index = (start + (i ** 2)) % self.table_size
        return None

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size


    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.get_num_items() / self.table_size

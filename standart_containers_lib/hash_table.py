from linked_list import LinkedList

class HashTable:
    """
    A hash table implementation using separate chaining with linked lists for collision handling.

    Attributes:
        size (int): The size of the hash table.
        table (list of LinkedList): The hash table implemented as an array of linked lists.

    Methods:
        __init__(size=10):
            Initializes the hash table with a specified size.
        _hash(key):
            Computes the hash value for a given key.
        insert(key, value):
            Inserts a key-value pair into the hash table. If the key already exists, updates the value.
        get(key):
            Retrieves the value associated with a given key from the hash table. Returns None if the key is not found.
        delete(key):
            Deletes the key-value pair associated with a given key from the hash table. Returns True if the deletion is successful, False otherwise.
        __iter__():
            Returns an iterator over the key-value pairs in the hash table.
    """
    
    def __init__(self, size=10):
        self.size = size
        self.table = [LinkedList() for _ in range(self.size)]

    def _hash(self, key):
        # линейное глупое хэширование
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if not self.table[index].update(key, value):
            self.table[index].insert(key, value)

    def get(self, key):
        index = self._hash(key)
        return self.table[index].find(key)

    def delete(self, key):
        index = self._hash(key)
        return self.table[index].delete(key)

    def __iter__(self):
        for linked_list in self.table:
            for key, value in linked_list:
                yield key, value

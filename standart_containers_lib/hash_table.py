from linked_list import LinkedList

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [LinkedList() for _ in range(self.size)]

    def _hash(self, key):
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

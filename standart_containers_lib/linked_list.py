class Node:
    """
    A singly linked list implementation to store key-value pairs for handling collisions in a hash table.

    Attributes:
        head (Node): The head node of the linked list.

    Methods:
        __init__():
            Initializes an empty linked list.
        insert(key, value):
            Inserts a new key-value pair at the end of the linked list.
        find(key):
            Finds the value associated with the given key in the linked list. Returns None if the key is not found.
        delete(key):
            Deletes the node with the given key from the linked list. Returns True if the deletion is successful, False otherwise.
        update(key, value):
            Updates the value of the node with the given key in the linked list. Returns True if the update is successful, False otherwise.
        __iter__():
            Returns an iterator over the key-value pairs in the linked list.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        current = self.head
        previous = None
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def update(self, key, value):
        current = self.head
        while current:
            if current.key == key:
                current.value = value
                return True
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current:
            yield current.key, current.value
            current = current.next

# '''
# Linked List hash table key/value pair
# '''
from typing import Tuple, List, Any, Union


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTableArray:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity: int) -> int:
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key) -> int:
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value) -> None:
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            print(f"WARNING: Collision has occured, at {index}")
        else:
            self.storage[index] = (key, value)
            print("Key-value successfully stored.")

    def remove(self, key) -> Union[Tuple[int, Any], None]:
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        old_item = None

        if self.storage[index] is not None:
            if self.storage[index][0] == key:
                old_item = self.storage[index]
                self.storage[index] = None
            else:
                print(f"WARNING: Collision has occured at {index}")
        else:
            print(f"WARNING: key {key} not found")

        return old_item

    def retrieve(self, key) -> Union[Any, None]:
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            if self.storage[index][0] == key:
                return self.storage[index][1]
            else:
                print(f"WARNING: Collision has occured at {index}")
        else:
            return None

        return None

    def resize(self) -> None:
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage[:]
        print(old_storage)
        self.capacity *= 2
        self.storage = [None] * self.capacity  # None 16x in an array

        for item in old_storage:
            if item is not None:
                self.insert(item[0], item[1])

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''

        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity

    def insert(self, key, value) -> None:
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)

        # add to the head of the list if index is not None
        if self.storage[index] is not None:
            # create a new node
            new_node = LinkedPair(key, value)
            # refrence the next node of the new node to be the current head
            new_node.next = self.storage[index]
            # set the array index to be the newly created node
            self.storage[index] = new_node
            print(f"WARNING: Collision has occured, at {index}, creating a new node")
            return None
        else:
            self.storage[index] = LinkedPair(key, value)
            return None

    def remove(self, key) -> None:
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_node = self.storage[index]
        prev_node = None

        # IF we have a match at the head of the LL
        if current_node.key == key:
            self.storage[index] = current_node.next

        if current_node.key != key:  # traverse the linked list
            while current_node.next is not None:
                # current node before we move
                prev_node = current_node  # line_1, 7
                # move forward
                current_node = current_node.next
                if current_node.key == key:
                    prev_node.next = current_node.next
                    return None
            print(f"WARNING: Key {key} not found")

    def retrieve(self, key) -> Union[None, Any]:
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_node = self.storage[index]

        if current_node is None:
            return None
        elif current_node.key == key:
            return current_node.value

        if current_node.key != key:
            while current_node.next is not None:
                current_node = current_node.next
                if current_node.key == key:
                    return current_node.value
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity  # None 16x in an array
        current_item = None
        for item in old_storage:
            current_item = item
            while current_item is not None:
                self.insert(current_item.key, current_item.value)
                current_item = current_item.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    print("Test if data intact after resizing")
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # print("")

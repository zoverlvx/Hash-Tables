# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# this is with the use of a tuple and doesn't use the LinkedPair
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
        # hashes key into an integer
        return hash(key)

    def _hash_djb2(self, key) -> int:
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # double-check this
        hash = 5381
        for n in key:
            hash = ((hash << 5) + hash) + ord(n)  # "<<" == x(2^y)
        return hash

    def _hash_mod(self, key: int) -> int:
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        # return self._hash_djb2(key) % self.capacity
        return self._hash(key) % self.capacity

    def insert(self, key: int, value: str) -> None:
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        
        if self.storage[index] is not None:
            print(F"WARNING: Collision has occurred at index {index}")
            return None
        else: 
            self.storage[index] = (key, value)
            print("Key-value inserted.")
            return None

    
    def remove(self, key: int) -> None:
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            if self.storage[index][0] == key:
                self.storage[index] = None
            else: 
                print(F"WARNING: Collision has occurred at index {index}")
                return None
        else:
            print(F"WARNING: key {key} not found")

        return None

    def retrieve(self, key: int) -> str | None:
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            # if the value at the index has a tuple there
            # and the key matches with the arg
            if self.storage[index][0] == key:
                # return the value
                return self.storage[index][1]
            else:
                print(F"WARNING: Collision has occurred at index {index}")
                return None
        else:
            return None


    def resize(self) -> None:
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # makes a copy of the current values in storage
        old_storage = self.storage[:]
        # updates capacity to be twice what it currently is
        self.capacity *= 2
        # rewrites storage with the updated capacity of key-values allowed
        self.storage = [None] * self.capacity
        # places old storage items into the new storage at the same indices
        # they were at formerally
        for item in old_storage:
            self.insert(item[0], item[1])


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    ht.insert("line_4", "4")
    ht.insert("line_5", "5")
    ht.insert("line_6", "6")
    ht.insert("line_7", "7")
    ht.insert("line_8", "8")
    ht.insert("line_9", "9")

    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")

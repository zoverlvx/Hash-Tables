class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count == self.capacity:
            # TODO: increase size
            print("Error: array is full")
            return
        if index >= self.count:
            # TODO: better error handling
            print("Error: index out of bounds")
            return 
        # counting backwards in storage from the most recently used index till
        # the index specified for insertion
        for i in range(self.count, index, -1):
            # move all current values down an index
            self.storage[i] = self.storage[i - 1]
        # store new value in specified index    
        self.storage[index] = value
        # count of number of values in table increased
        self.count += 1
    
    def append(self, value):
        if self.count == self.capacity:
            print("Error: Array is full.")
            return
        # stores the value in the last unused index
        self.storage[self.count] = value
        self.count += 1

    def double_size(self):
        self.capacity *= 2 # doubles capacity
        # creates new storage by the number of capacity
        new_storage = [None] * self.capacity
        # places values from former storage into new storage
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        # removes old storage and replaces it with the new storage
        self.storage = new_storage

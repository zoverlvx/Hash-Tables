import random


def collisions(buckets, loops=1):
    '''
    Roll random hash indexes into buckets and pring
    how many rolls befor a hash collision

    Run loops number of times
    '''
    for i in range(loops):
        tries = 0
        tried = set()
        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1
            else:
                # found a collision
                break
        print(f"{buckets} buckets, tries {tries} hashes before collision. ({tries / buckets * 100:.1f}%)")


# collisions(32, 10)


def longest_linked_list_chain(keys, buckets, loops=10):

    '''
    Rolls keys number of random keys into buckets, buckets and cound the collisions

    Run loops times
    '''

    for i in range(loops):
        key_counts = {}

        for i in range(buckets):
            key_counts[i] = 0

        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1

        largest_n = 0
        for key in key_counts:
            if key_counts[key] > largest_n:
                largest_n = key_counts[key]

        print(f"longest linked list chain for {keys} keys in buckets {buckets} with a load factor of (Load factor: {keys / buckets:2f}: {largest_n})")


longest_linked_list_chain(16, 16, 10)

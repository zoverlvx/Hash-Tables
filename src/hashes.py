import hashlib

# creates a binary string
key = b"mom"

# another way to encode
new_string = "Just another string".encode()

for i in range(10):
    hashed = hashlib.sha256(key).hexdigest()
    print(hashed)

for i in range(10):
    # another way to hash something
    hashed = hash(key)
    print(hashed % 8)

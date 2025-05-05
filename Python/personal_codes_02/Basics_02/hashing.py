import hashlib

data = "192.168.1.5:55555"
print(data)
print(data.encode()) # returns b'192.168.1.5:55555'

address = "192.168.1.10:56789"
hash = hashlib.sha1(address.encode()).hexdigest()[:8]
print(hash.upper())  # e.g., "5F2B8C1D"

hash_obj = hashlib.sha1(b"192.168.1.5:55555")
print(hash_obj)

hash_obj2 = hashlib.sha256(b"192.168.1.5:55555")
print(hash_obj2)

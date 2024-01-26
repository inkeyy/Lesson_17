import hashlib
hash_ob = hashlib.md5(b"Hello World")
print(hash_ob.hexdigest())
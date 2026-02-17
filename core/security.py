import hashlib

def hash_value(value: str):
    return hashlib.sha256(value.encode()).hexdigest()

def verify_hash(value: str, hashed: str):
    return hash_value(value) == hashed

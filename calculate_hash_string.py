import hashlib


def calculate_hash_string(text, hash_algorithm='sha256'):
    hash_object = hashlib.new(hash_algorithm)
    hash_object.update(text.encode())
    return hash_object.hexdigest()


hash_string = calculate_hash_string(text='Hello, World!')
print(f'Hash value for string: {hash_string}')

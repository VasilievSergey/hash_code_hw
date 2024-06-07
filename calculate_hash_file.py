import hashlib


def calculate_hash_file(file_path, hash_algorithm='sha256'):
    hash_object = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        while chunk := file.read(4096):
            hash_object.update(chunk)
    return hash_object.hexdigest()


file_path = 'file.txt'
hash_file = calculate_hash_file(file_path)
print(f'Hash value for file: {hash_file}')

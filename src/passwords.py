from hashlib import pbkdf2_hmac
from os import urandom


hash_name = 'sha256'
iterations = 100_000
dk_len = 126

salt_size = 32
salt = urandom(salt_size)

password = b'very_bad_password'
hash = pbkdf2_hmac(hash_name, password, salt, iterations, dk_len)


import string

def encrypt(plaintext, key_map):
    alphabet = string.ascii_uppercase
    plaintext = plaintext.upper()
    table = str.maketrans(alphabet, key_map)
    return plaintext.translate(table)

def decrypt(ciphertext, key_map):
    alphabet = string.ascii_uppercase
    ciphertext = ciphertext.upper()
    rev_map = str.maketrans(key_map, alphabet)
    return ciphertext.translate(rev_map)

def example_key():
    # Simple key map for testing (can randomize later)
    return "QWERTYUIOPASDFGHJKLZXCVBNM"

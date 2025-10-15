def decrypt(ciphertext, key):
    return ''.join(chr(ord(c) ^ key) for c in ciphertext)

def brute_force(ciphertext):
    results = {}
    for key in range(1, 256):
        try:
            plain = decrypt(ciphertext, key)
            results[key] = plain
        except:
            continue
    return results

def decrypt(ciphertext, shift):
    result = ""
    for ch in ciphertext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base - shift) % 26 + base)
        else:
            result += ch
    return result

def brute_force(ciphertext):
    return {shift: decrypt(ciphertext, shift) for shift in range(1, 26)}

from ciphers import Cipher

CIPHER_GRID = {
    'A': 11,
    'B': 12,
    'C': 13,
    'D': 14,
    'E': 15,
    'F': 16,
    'G': 21,
    'H': 22,
    'I': 23,
    'J': 24,
    'K': 25,
    'L': 26,
    'M': 31,
    'N': 32,
    'O': 33,
    'P': 34,
    'Q': 35,
    'R': 36,
    'S': 41,
    'T': 42,
    'U': 43,
    'V': 44,
    'W': 45,
    'X': 46,
    'Y': 51,
    'Z': 52,
    ' ': 53,
    '1': 54,
    '2': 55,
    '3': 56,
    '4': 61,
    '5': 62,
    '6': 63,
    '7': 64,
    '8': 65,
    '9': 66,
    '0': 71
}

class Polybius(Cipher):

    def encrypt(self, text, cipher_pad):
        text = text.upper()
        cipher_pad = cipher_pad.upper()
        encrypted_code = []
        to_be_encrypted_message = list(text)
        to_be_encrypted_cipher_pad = list(cipher_pad)
        for char in to_be_encrypted_message:
            encrypted_code.append(str(CIPHER_GRID[char]))
        for char in to_be_encrypted_cipher_pad:
            encrypted_code.append(str(CIPHER_GRID[char]))
        return ' '.join(encrypted_code)

    def decrypt(self, text, cipher_pad):
        text = text.upper()
        cipher_pad = cipher_pad.upper()
        decrypted_text = []
        to_be_decrypted_hash = text.split()
        for char in to_be_decrypted_hash:
            decrypted_text.append(CIPHER_GRID.keys()[CIPHER_GRID.values().index(int(char))])
        cipher_pad_length = len(cipher_pad)
        actual_cipher_pad = ''.join(decrypted_text[-cipher_pad_length:])
        if cipher_pad == actual_cipher_pad:
            del decrypted_text[-cipher_pad_length:]
            return ''.join(decrypted_text)
        else:
            return "Incorrect Cipher Pad. Intruder! Activate machine gun turrets!"


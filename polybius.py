from ciphers import Cipher


class Polybius(Cipher):

    def __init__(self):
        self.cipher_grid = {
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

    def encrypt(self, text, cipher_pad):
        """
        Takes to-be-encrypted-text and a unique alphanumerical cipher-pad as arguments
        The text gets encrypted using a dictionary. The cipher-pad gets
        encrypted and added at the end of the text string.
        Returns a series of 2 digit numbers as a string object.
        """
        text = text.upper()
        cipher_pad = cipher_pad.upper()
        encrypted_code = []
        to_be_encrypted_message = list(text)
        to_be_encrypted_cipher_pad = list(cipher_pad)
        for char in to_be_encrypted_message:
            encrypted_code.append(str(self.cipher_grid[char]))
        for char in to_be_encrypted_cipher_pad:
            encrypted_code.append(str(self.cipher_grid[char]))
        return ' '.join(encrypted_code)

    def decrypt(self, text, cipher_pad):
        """
        Takes to-be-decrypted text (a series of 2 digit numbers as strings) and the
        same unique alphanumerical cipher-pad that was used to encrypt the original message.
        The message and the cipher-pad both are decrypted, and the cipher-pad is removed
        from the end of the decrypted message. If the given cipher-pad and
        the decrypted cipher-pad match, the decrypted message is returned as a string object
        """
        text = text.upper()
        cipher_pad = cipher_pad.upper()
        decrypted_text = []
        to_be_decrypted_hash = text.split()
        for char in to_be_decrypted_hash:
            decrypted_text.append(self.cipher_grid.keys()[self.cipher_grid.values().index(int(char))])
        cipher_pad_length = len(cipher_pad)
        actual_cipher_pad = ''.join(decrypted_text[-cipher_pad_length:])
        if cipher_pad == actual_cipher_pad:
            del decrypted_text[-cipher_pad_length:]
            return ''.join(decrypted_text)
        else:
            return "Incorrect Cipher Pad. Intruder! Activate machine gun turrets!"

import string

from ciphers import Cipher


class Caesar(Cipher):
    FORWARD = string.ascii_uppercase * 3

    def __init__(self, offset=3):
        self.offset = offset
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase

    def encrypt(self, text, cipher_pad):
        output = []
        text = text.upper() + cipher_pad.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])

        return ''.join(output)

    def decrypt(self, text, cipher_pad):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        cipher_pad_length = len(cipher_pad)
        actual_cipher_pad = ''.join(output[-cipher_pad_length:])
        if cipher_pad.upper() == actual_cipher_pad:
            del output[-cipher_pad_length:]
            return ''.join(output)
        else:
            return "Incorrect Cipher Pad. Intruder! Activate machine gun turrets!"

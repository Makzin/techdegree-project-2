from ciphers import Cipher


class AtBash(Cipher):

    def __init__(self):
        self.regular = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890'
        self.reverse = 'ZYXWVUTSRQPONMLKJIHGFEDCBA 0987654321'

    def encrypt(self, text, cipher_pad):
        text = text.upper()
        encrypted_message = []
        cipher_pad = cipher_pad.upper()
        to_be_encrypted_message = list(text)
        to_be_encrypted_cipher_pad = list(cipher_pad)
        encrypt_key = dict(zip(self.regular, self.reverse))
        for char in to_be_encrypted_message:
            encrypted_message.append(encrypt_key[char])
        for char in to_be_encrypted_cipher_pad:
            encrypted_message.append(encrypt_key[char])
        return ''.join(encrypted_message)


    def decrypt(self, text, cipher_pad):
        text = text.upper()
        decrypted_text = []
        cipher_pad = cipher_pad.upper()
        to_be_decrypted_message = list(text)
        decrypt_key = dict(zip(self.reverse, self.regular))
        for char in to_be_decrypted_message:
            decrypted_text.append(decrypt_key[char])
        cipher_pad_length = len(cipher_pad)
        actual_cipher_pad = ''.join(decrypted_text[-cipher_pad_length:])
        if cipher_pad == actual_cipher_pad:
            del decrypted_text[-cipher_pad_length:]
            return ''.join(decrypted_text)
        else:
            return "Incorrect Cipher Pad. Intruder! Activate machine gun turrets!"


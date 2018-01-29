from ciphers import Cipher


class AtBash(Cipher):

    def __init__(self):
        self.regular = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890'
        self.reverse = 'ZYXWVUTSRQPONMLKJIHGFEDCBA 0987654321'

    def encrypt(self, text, cipher_pad):
        """Takes to-be-encrypted-text and a unique alphanumerical cipher-pad as arguments
        The text gets encrypted using 2 lists. The cipher-pad gets encrypted and added
        at the end of the text string.
        Returns a series of encoded characters in a string object """
        text = text.upper()
        encrypted_message = []
        cipher_pad = cipher_pad.upper()
        to_be_encrypted_message = list(text)
        to_be_encrypted_cipher_pad = list(cipher_pad)
        encrypt_key = dict(zip(self.regular, self.reverse))
        for char in to_be_encrypted_message:
            encrypted_message.append(encrypt_key[char])
        # Adds the encrypted cipher pad to the end of the encrypted message
        for char in to_be_encrypted_cipher_pad:
            encrypted_message.append(encrypt_key[char])
        return ''.join(encrypted_message)

    def decrypt(self, text, cipher_pad):
        """
        Takes to-be-decrypted text (a series of 2 digit numbers as strings) and
        the same unique alphanumerical cipher-pad that was used to encrypt the original message.
        The message and the cipher-pad both are decrypted, and the cipher-pad is removed
        from the end of the decrypted message. If the given cipher-pad and the decrypted cipher-pad match,
        the decrypted message is returned as a string object.
        """
        text = text.upper()
        decrypted_text = []
        cipher_pad = cipher_pad.upper()
        to_be_decrypted_message = list(text)
        decrypt_key = dict(zip(self.reverse, self.regular))
        for char in to_be_decrypted_message:
            decrypted_text.append(decrypt_key[char])
        # Grabs the encrypted cipher-pad using the length of the given cipher-pad.
        # If the given cipher-pad is incorrect, this will fail.
        cipher_pad_length = len(cipher_pad)
        actual_cipher_pad = ''.join(decrypted_text[-cipher_pad_length:])
        # Decrypted message is only accurate and will only be given if the given cipher-pad
        # matches the cipher pad used to encrypt the original message
        if cipher_pad == actual_cipher_pad:
            del decrypted_text[-cipher_pad_length:]
            return ''.join(decrypted_text)
        else:
            return "Incorrect Cipher Pad. Intruder! Activate machine gun turrets!"

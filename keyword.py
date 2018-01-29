from ciphers import Cipher


class Keyword(Cipher):

    def __init__(self):
        self.plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 '

    def encrypt(self, text, cipher_pad):
        """
        Accepts an alphanumerical string object (text) and an alphanumerical string object (cipher_pad)
        as arguments.
        Uses 2 lists to encrypt the original text given.
        Returns a string object containing alphanumerical characters
        """
        # Converts all input to lists, adds the cipher_pad to the beginning of an alphanumerical list.
        text = text.upper()
        cipher_pad = cipher_pad.upper()
        to_be_encrypted_message = list(text)
        regular_alphabet = list(self.plaintext)
        ciphered_alphabet = list(cipher_pad) + regular_alphabet
        # The alphanumerical list containing the cipher_pad is sorted to remove duplicates
        filtered_alphabet = []
        for char in ciphered_alphabet:
            if char not in filtered_alphabet:
                filtered_alphabet.append(char)
        cipher_dict = {}
        # Dictionary is used to map the encoded list against a regular alphabet list.
        for cipher_char in filtered_alphabet:
            index = filtered_alphabet.index(cipher_char)
            regular_char = regular_alphabet[index]
            cipher_dict[regular_char] = cipher_char
        # The mapped dictionary is used to encrypt the text message.
        encrypted_message = []
        for char in to_be_encrypted_message:
            if char in cipher_dict.values():
                encrypted_message.append(cipher_dict[char])
        return ''.join(encrypted_message)

    def decrypt(self, text, cipher_pad):
        """Accepts an alphanumerical string object (text) and an alphanumerical string object (cipher_pad)
        as arguments.
        Uses 2 lists to decrypt the encrypted text given.
        Returns a string object containing alphanumerical characters"""
        # Very similar logic to the encryption algorithm, but the dictionary is switched
        # to contain the opposite order of characters.
        # Converts all input to lists, adds the cipher_pad to the beginning of an alphanumerical list.
        text = text.upper()
        cipher_pad = cipher_pad.upper()
        to_be_decrypted_message = list(text)
        regular_alphabet = list(self.plaintext)
        ciphered_alphabet = list(cipher_pad) + regular_alphabet
        # The alphanumerical list containing the cipher_pad is sorted to remove duplicates
        filtered_alphabet = []
        for char in ciphered_alphabet:
            if char not in filtered_alphabet:
                filtered_alphabet.append(char)
        # Dictionary is used to map the regular alphabet list against the encoded list
        cipher_dict = {}
        for cipher_char in filtered_alphabet:
            index = filtered_alphabet.index(cipher_char)
            regular_char = regular_alphabet[index]
            cipher_dict[cipher_char] = regular_char
        # The mapped dictionary is used to decrypt the text message.
        decrypted_message = []
        for char in to_be_decrypted_message:
            if char in cipher_dict.values():
                decrypted_message.append(cipher_dict[char])
        return ''.join(decrypted_message)

from ciphers import Cipher

PLAINTEXT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 '

class Keyword(Cipher):

    def encrypt(self, text, cipher_pad):
        text = text.upper()
        cipher_pad = cipher_pad.upper()
        to_be_encrypted_message = list(text)
        regular_alphabet = list(PLAINTEXT)
        ciphered_alphabet = list(cipher_pad) + regular_alphabet
        filtered_alphabet = []
        for char in ciphered_alphabet:
            if char not in filtered_alphabet:
                filtered_alphabet.append(char)
        cipher_dict = {}
        for cipher_char in filtered_alphabet:
            index = filtered_alphabet.index(cipher_char)
            regular_char = regular_alphabet[index]
            cipher_dict[regular_char] = cipher_char
        encrypted_message = []
        for char in to_be_encrypted_message:
            if char in cipher_dict.values():
                encrypted_message.append(cipher_dict[char])
        return ''.join(encrypted_message)


    def decrypt(self, text, cipher_pad):
        text = text.upper()
        cipher_pad = cipher_pad.upper()
        to_be_decrypted_message = list(text)
        regular_alphabet = list(PLAINTEXT)
        ciphered_alphabet = list(cipher_pad) + regular_alphabet
        filtered_alphabet = []
        for char in ciphered_alphabet:
            if char not in filtered_alphabet:
                filtered_alphabet.append(char)
        cipher_dict = {}
        for cipher_char in filtered_alphabet:
            index = filtered_alphabet.index(cipher_char)
            regular_char = regular_alphabet[index]
            cipher_dict[cipher_char] = regular_char
        decrypted_message = []
        for char in to_be_decrypted_message:
            if char in cipher_dict.values():
                decrypted_message.append(cipher_dict[char])
        return ''.join(decrypted_message)

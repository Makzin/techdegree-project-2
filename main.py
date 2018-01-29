from atbash import AtBash
from caesar import Caesar
from keyword import Keyword
import time
from polybius import Polybius


def encrypt(string, cipher, cipher_pad):
    if cipher == 'atbash':
        atbash = AtBash()
        return atbash.encrypt(string, cipher_pad)
    elif cipher == 'caesar':
        caesar = Caesar()
        return caesar.encrypt(string, cipher_pad)
    elif cipher == 'polybius':
        polybius = Polybius()
        return polybius.encrypt(string, cipher_pad)
    elif cipher == 'keyword':
        keyword = Keyword()
        return keyword.encrypt(string, cipher_pad)


def decrypt(string, cipher, cipher_pad):
    if cipher == 'atbash':
        atbash = AtBash()
        return atbash.decrypt(string, cipher_pad)
    elif cipher == 'caesar':
        caesar = Caesar()
        return caesar.decrypt(string, cipher_pad)
    elif cipher == 'polybius':
        polybius = Polybius()
        return polybius.decrypt(string, cipher_pad)
    elif cipher == 'keyword':
        keyword = Keyword()
        return keyword.decrypt(string, cipher_pad)


def main():
    print("Welcome to the Cipher Tool, Agent!")
    choice_encrypt = None
    choice_decrypt = None
    while True:
        print("Would you like to encrypt or decrypt?")
        print("(1) - Encrypt")
        print("(2) - Decrypt")
        user_answer = raw_input()
        if (user_answer == '1') or (user_answer.lower() == 'encrypt'):
            choice_encrypt = True
            break
        elif (user_answer == '2') or (user_answer.lower() == 'decrypt'):
            choice_decrypt = True
            break
        else:
            print("That is not a valid choice. Please try again?")

    while True:
        print("Please choose your Cipher: ")
        print("(1) - Atbash")
        print("(2) - Caesar")
        print("(3) - Polybius")
        print("(4) - Keyword")
        user_answer = raw_input()
        if (user_answer == '1') or (user_answer.lower() == 'atbash'):
            cipher_to_use = 'atbash'
            break
        elif (user_answer == '2') or (user_answer.lower() == 'caesar'):
            cipher_to_use = 'caesar'
            break
        elif (user_answer == '3') or (user_answer.lower() == 'polybius'):
            cipher_to_use = 'polybius'
            break
        elif (user_answer == '4') or (user_answer.lower() == 'keyword'):
            cipher_to_use = 'keyword'
            break
        else:
            print("That is not a valid choice. Please try again?")

    while True:
        print("What word or sentence would you like to use?")
        chosen_string = raw_input()
        if chosen_string != '':
            break

    while True:
        print("What is your unique cipher pad?")
        cipher_pad = raw_input()
        if cipher_pad != '':
            break

    if choice_encrypt:
        result = encrypt(chosen_string, cipher_to_use, cipher_pad)
        print("Your encrypted code is:")
        print(result)
    else:
        result = decrypt(chosen_string, cipher_to_use, cipher_pad)
        print("Your decrypted message is:")
        print(result)

    while True:
        time.sleep(1)
        print('Anything else you would like to do today?')
        print('(1) - Yes')
        print('(2) - No')
        answer = raw_input()
        if answer == '1' or answer.lower() == 'yes':
            main()
        elif answer == '2' or answer.lower() == 'no':
            print('Thanks for using the Cipher Tool, Agent. Stay safe!')
            time.sleep(1)
            print('For security reasons, this program will self destruct in: ')
            time.sleep(1)
            for i in list(range(5))[::-1]:
                print(i + 1)
                time.sleep(1)
            print("Boom! Good Bye!")
            break
        else:
            print('Incorrect answer. Please try again!')
        break

main()

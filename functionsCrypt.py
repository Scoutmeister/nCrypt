from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from colorama import init, Fore
import base64
from base64 import b64encode
import random
import os


class Crypter():

    def __init__(self, filename, mode, anon, password):
        self.filename = filename
        self.mode = mode
        self.anon = anon
        self.password = password
        self.key = self.load_key(self.password)

    ## Color output methods ##
    def color_green(self, text):
        return Fore.GREEN + text
    # Returns red text    
    def color_red(self, text):
        return Fore.RED + text

    ## Method for loading key into object ##
    def load_key(self, pwd):

        salt = b"\xec"
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=480000)
        pwd = b64encode(bytes(pwd, "ASCII"))
        key = base64.urlsafe_b64encode(kdf.derive(pwd))
        cipher_suite = Fernet(key)
        return cipher_suite

    ## Method for encrypting file
    def encrypt_file(self):
        filename = self.filename

        try:
            # Reads the content of the file and saves it
            with open(filename, "rb") as file:
                plaintext = file.read()

            # Creates name for the new encrypted file
            if self.anon:
                encryptedFileName = str(random.randint(1,10000000)) + ".enc"
            else:
                encryptedFileName = filename.split(".")[0] + ".enc"
            os.remove(filename)

            # Encrypt the plaintext and replace it with ciphertext. Add encrypted filename to the end
            with open(encryptedFileName, "wb") as file:
                cipher_text = self.key.encrypt(plaintext)
                originalFileNameEncrypt = self.key.encrypt(filename.encode())
                file.writelines([cipher_text, "\n".encode(),originalFileNameEncrypt])

            print(self.color_green(f"The file '{filename}' has been encrypted to: {encryptedFileName}"))
        #Error handling
        except FileNotFoundError:
            print(self.color_red("File not found, make sure to include the full file name(example.txt)"))

    ## Method for decrypting file
    def decrypt_file(self):
        filename = self.filename

        try:
            # Reads the content of the file and saves it
            with open(filename, "rb") as file:
                cipher_text = file.readlines()

            # Creates name for the new decrypted file
            decryptedFileName = self.key.decrypt(cipher_text[1])
            os.remove(filename)

            # Decrypts the ciphertext and replace it with plaintext
            with open(decryptedFileName, "wb") as file:
                plaintext = self.key.decrypt(cipher_text[0].strip())
                file.write(plaintext)
        # Error handling
        except FileNotFoundError:
            print(self.color_red("File not found, make sure to include the full file name(example.enc)"))
        # Error for if key can't decrypt the file
        except Exception:
                print(self.color_red("Error! Can't decrypt file with key provided, did you type the right password?"))
                exit()
        print(self.color_green(f"The file '{filename}' has been decrypted to: {decryptedFileName.decode()}"))

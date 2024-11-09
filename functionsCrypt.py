from cryptography.fernet import Fernet
from colorama import init, Fore
import random
import os


class Crypter():

    def __init__(self, filename, mode, newkey, anon):
        self.filename = filename
        self.mode = mode
        self.newkey = newkey
        if self.newkey and mode != "decrypt":
            self.gen_key()
            print(self.color_green("Generating new key"))
        elif self.newkey and mode == "decrypt":
            print(self.color_red("For safety purposes you can't change the key before decryption"))
            exit()
        else:
            pass
        self.anon = anon
        self.key = self.load_key()

    ## Color output methods ##
    def color_green(self, text):
        return Fore.GREEN + text
    # Returns red text    
    def color_red(self, text):
        return Fore.RED + text

    ## Method for generating new key ##
    def gen_key(self):
        key = Fernet.generate_key()

        with open("secret.key", "wb") as file:
            file.write(key)

    ## Method for loading key into object ##
    def load_key(self):

        if os.path.exists("secret.key"):
            # Loads the encryption key from secret.key
            with open("secret.key", "rb") as file:
                key = file.read()

            # Creates a Fernet object with the key
            cipher_suite = Fernet(key)
            return cipher_suite
        else:
            self.gen_key()
            print(self.color_green("No excisting key found, creating key"))
            return self.load_key()


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
            # Loads the encryption key from secret.key

        try:
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
            print(self.color_green(f"The file '{filename}' has been decrypted to: {decryptedFileName.decode()}"))
        # Error for if key can't decrypt the file
        except Exception:
                print(self.color_red("Error! Can't decrypt file with key provided."))
                exit()

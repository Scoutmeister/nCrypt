from cryptography.fernet import Fernet
import os

## Generate key ##
def gen_key(keyfilename):
    key = Fernet.generate_key()

    with open(keyfilename + ".key", "wb") as file:
        file.write(key)

# Loads the encryption key from secret.key
with open("secret.key", "rb") as file:
    key = file.read()

# Creates a Fernet object with the key
cipher_suite = Fernet(key)

## Encryption ##
def encrypt_file(filename):

    try:
        # Reads the content of the file and saves it
        with open(filename, "rb") as file:
            plaintext = file.read()

        # Creates name for the new encrypted file
        encryptedFileName = filename.split(".")[0] + ".enc"
        os.remove(filename)

        # Encrypt the plaintext and replace it with ciphertext
        with open(encryptedFileName, "wb") as file:
            cipher_text = cipher_suite.encrypt(plaintext)
            file.write(cipher_text)
    except FileNotFoundError:
        print("File not found, make sure to include the full file name(example.txt)")
    


## Decryption ##
def decrypt_file(filename):

    try:
        # Reads the content of the file and saves it
        with open(filename, "rb") as file:
            cipher_text = file.read()

        # Creates name for the new decrypted file
        decryptedFileName = filename.split(".")[0] + ".txt"
        os.remove(filename)

        # Decrypts the ciphertext and replace it with plaintext
        with open(decryptedFileName, "wb") as file:
            plaintext = cipher_suite.decrypt(cipher_text)
            file.write(plaintext)
    #Error handling
    except FileNotFoundError:
        print("File not found, make sure to include the full file name(example.enc)")


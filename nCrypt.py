from functionsCrypt import Crypter, init
import argparse

# Creating argument parser
parser = argparse.ArgumentParser(description="My file encryption/decrytion program")
# Adding arguments 
parser.add_argument("filename", help="Enter the name of the file you want to use(include file extention)")
parser.add_argument("-m", "--mode", choices=["encrypt", "decrypt"], help="Choose mode. The default mode is 'encrypt' if flag is not present")
parser.add_argument("-a", "--anonymous", action="store_true", help="Creates random encrypted file name if flag is present, does nothing if mode is decrypt")
parser.add_argument("-p", "--password", required=True, help="Password from which the key is derived from")
args = parser.parse_args()

# Initializing colorama
init()

# Creating Crypter object with argparse inputs
krypt = Crypter(args.filename, args.mode, args.anonymous, args.password)

if krypt.mode == "encrypt" or krypt.mode == None:
    krypt.encrypt_file()
elif krypt.mode == "decrypt":
    krypt.decrypt_file()

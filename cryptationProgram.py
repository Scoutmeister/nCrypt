from functionsCrypt import *
import argparse

parser = argparse.ArgumentParser(description="File encryption/decrytion program")
###### Lägg till arguments för varje flagga (-e, -d, -k) och lista ut hur man tar inputs efter flaggor. OBS borde alltid kolal efter -k först efterssom man inte kan göra de andra utan nyckel
parser.add_argument("filename", help="Enter the name of the file you want to use(include file extention)")
parser.add_argument("-m", "--mode", help="Choose between 'encrypt' and 'decrypt'")
parser.add_argument("-k", "--key", action="store_true", help="This flag generates a new encryption key")
args = parser.parse_args()

accepted_modes = ["encrypt", "decrypt"]

if args.mode in accepted_modes:

    # Adding a safety net so that you don't change the key you used to encrypt with
    if args.key and args.mode != "decrypt":
        gen_key()
        print("Generating new key")
    elif args.key and args.mode == "decrypt":
        print("For safety purposes you can't change the key before decryption")
        exit()
    else: pass


    # Runs if encryption mode is chosen
    if args.mode == "encrypt":
        if os.path.exists("secret.key"):
            encrypt_file(args.filename)
        else:
            gen_key()
            print("No excisting key found, creating key")
            encrypt_file(args.filename)     
    elif args.mode == "decrypt":
        if os.path.exists("secret.key"):
            decrypt_file(args.filename)
        else: print("Something has gone wrong. Key used for encryption not found")

else:
    print("Please use the -m or --mode flag to choose a valid mode")



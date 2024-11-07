from functionsCrypt import *
import argparse

# Creating argument parser
parser = argparse.ArgumentParser(description="File encryption/decrytion program")
# Adding arguments 
parser.add_argument("filename", help="Enter the name of the file you want to use(include file extention)")
parser.add_argument("-m", "--mode", help="Choose between 'encrypt' and 'decrypt'")
parser.add_argument("-k", "--key", action="store_true", help="This flag generates a new encryption key")
#### Lägg til -a --anon argument för att spela filen med ett annat namn när den är krypterad
args = parser.parse_args()

# Initializing colorama
init()

# Specifying accepted inputs for --mode
accepted_modes = ["encrypt", "decrypt"]

if args.mode in accepted_modes:

    # Adding a safety net so that you don't change the key you used to encrypt with
    if args.key and args.mode != "decrypt":
        gen_key()
        print(color_green("Generating new key"))
    elif args.key and args.mode == "decrypt":
        print(color_red("For safety purposes you can't change the key before decryption"))
        exit()
    else: pass


    # Runs if encryption mode is chosen
    if args.mode == "encrypt":
        if os.path.exists("secret.key"):
            encrypt_file(args.filename)
        else:
            gen_key()
            print(color_green("No excisting key found, creating key"))
            encrypt_file(args.filename)   
    # Runs if decryption mode is chosen  
    elif args.mode == "decrypt":
        if os.path.exists("secret.key"):
            decrypt_file(args.filename)
        else: print(color_red("Something has gone wrong. Key used for encryption not found"))
# Prints if the input isn't recognized
else:
    print(color_red("Please use the -m or --mode flag to choose a valid mode"))


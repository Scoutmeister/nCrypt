from functionsCrypt import *
import argparse

parser = argparse.ArgumentParser(description="File encryption/decrytion program")
###### Lägg till arguments för varje flagga (-e, -d, -k) och lista ut hur man tar inputs efter flaggor. OBS borde alltid kolal efter -k först efterssom man inte kan göra de andra utan nyckel
parser.add_argument("-e", "--encrypt", action="")
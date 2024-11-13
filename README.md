# 📦 nCrypt

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Wola_Gu%C5%82owska-trumna.jpg/220px-Wola_Gu%C5%82owska-trumna.jpg)


## 🌟 Highlights

- Simple tool for symmetric cryptography
- Features Encryption and Decryption
- Derives cryptography key from passwords
- Anonymous naming of encrypted files


## ℹ️ Overview

This is a simple tool made for encrypting and decrypting files run completely from the CLI. It reads the bytes in a file and encrypts/decrypts it using a key derived from a password. There is an option for anonymous naming of encrypted files to prevent sharing unwanted information. The default mode is encryption if the -m flag is not specified.

## 🚀 Usage

```bash
python nCrypt.py example.txt -a -p hello123
```
This command will encrypt the 'example.txt' file with a key derived from the password 'hello123', and give it an anonymous name.


## ⬇️ Installation

```bash
git clone https://github.com/Scoutmeister/nCrypt.git
```
Clone the github repo
```bash
pip install -r requirements.txt
```
Install the python packages needed for the program to run correctly

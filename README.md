# 📦 nCrypt

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Wola_Gu%C5%82owska-trumna.jpg/220px-Wola_Gu%C5%82owska-trumna.jpg)


## 🌟 Highlights

- Simple tool for symmetric cryptography
- Features Encryption and Decryption
- Anonymous naming of encrypted files
- Safety checks implemented to prevent accedental misuse


## ℹ️ Overview

This is a simple tool made for encrypting and decrypting files run completely from the CLI. It uses symmetric cryptography to read the byte information in any file and encrypt it. There is an option for anonymous naming of encrypted files to prevent sharing unwanted information. The default mode is encryption if the -m flag is not specified.

## 🚀 Usage

```bash
python nCrypt.py example.txt -m encrypt -a
```
This command will encrypt the 'example.txt' file and give it an anonymous name


## ⬇️ Installation

```bash
git clone https://github.com/Scoutmeister/nCrypt.git
```
Clone the github repo
```bash
pip install -r requirements.txt
```
Install the python packages needed for the program to run correctly

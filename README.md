# Two-Factor-Authentication-Python
Easy and Usable Two-Factor Authentication using Python

## Installation
run command ``pip install -r requirements.txt``

## How it works
1. Create a key using ``pyotp`` (recommended) or you can just write it manually (Only for testing purposes)
2. Create a **uri**
3. Use the *uri** to create a QRCode using ``qrcode`` library
4. Scan the QRCode using and authentication app like ``google authentication`` app
5. Test the 6 degits 

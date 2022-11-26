# Encryption
This is ransomware.

Do not use it for bad stuff.

This ransomeware is totally for educational purpuses.

I totally dont expect anybody to use it maliciously.

I am not responsible for anything anybody does with my software.

most importantly, have fun educting yourself and your victims.

The encoder1 file uses PyAES encryption.

encryptor v2.2 uses fernet, you will need to find a way to install Fernet on your victims machine:
```
pip install cryptography
```
The key used in the encrypt and decrypt files is the same every time, you can change them if you want. The setup.py file generates both files in the specified diectory, with the same password, and then runs the encryption file.

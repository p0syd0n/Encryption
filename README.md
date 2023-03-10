# Encryption
This is ransomware, purely educational and I do not expect it to work well enough to actuall be used.

It works by going through a directory, and adding each file's path to a list. It then goes through the list and encrypts each file. THe reason it doesn;t encrypt them right away is because I wanted a way to compare the amount of files that could be foun compared to the amount of files encrypted.

The encoder1 file uses PyAES encryption.

encryptor v2.2 uses fernet:
```
pip install cryptography
```
The key used in the encrypt and decrypt files is the same every time, you can change them if you want. The setup.py file generates both files in the specified diectory, with the same key,(new every time you run setup.py) and then runs the encryption file.

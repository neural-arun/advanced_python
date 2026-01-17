
# my_file = open("07_files_in_python/01_project/data.txt", "r")

# file_content = my_file.read()
# print(file_content)
# my_file.close()



from pathlib import Path

BASE_DIR = Path(__file__).parent  #__file__ ye hai current python file ka address and .parent hai us file ka folder.

file_path = BASE_DIR / "data.txt"    # data.txt same folder wali file

with open(file_path, "r") as f:
    content = f.read()
# Ye auto close bhi kar deta hai.
print(content)

name = input("Enter your name: ")
with open(file_path,'w') as f:
    content = f.write(name) # Ye number of characters written return karta hai.
    f.write(name)   # this is the right way to write in the file.

print(content)
    
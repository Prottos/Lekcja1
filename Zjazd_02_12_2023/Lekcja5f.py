import os
import time
from pathlib import Path

print(os.getcwd())
os.chdir(Path.home())
# print(os.getcwd())
# os.mkdir("Folder1")
# time.sleep(4)
# # print(os.environ)
# os.rename("Folder1", "Folder2")
# time.sleep(4)
# os.rmdir("Folder2")
# time.sleep(4)
# print("kupa")

os.system('cmd /c "cd C:\\Users\\Zimniok\\Desktop && ipconfig /all >> result.txt"')
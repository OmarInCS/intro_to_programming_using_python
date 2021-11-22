import os

path = "C:\\Users\\Mr Omar\\Desktop"
files = os.listdir(path)
for f in files:
    if f.endswith(".pdf"):
        print(path + "\\" + f)

# Printing Content of Directory 
import os

# Enter the path of the directory whose content you want to print
path = '/github'

# List all files and folders using os module 
contents = os.listdir(path)

# print the content of Directory 
print("\nContents of the directory are:")
for item in contents:
    print(item)

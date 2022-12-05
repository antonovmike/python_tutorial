"""
mkdir() - make directory
rmdir() - remove directory
rename() - rename file
remove() - remove file
"""

import os

# Create new folder in your project directory
# os.mkdir("hello")
# Create new folder at the specified address
# os.mkdir("/home/USER_NAME/Desktop/hello_2")

# Rename file
# os.rename("/home/mike/Desktop/some_file.txt", "/home/mike/Desktop/hello.txt")

# Remove file
# os.remove("/home/mike/Desktop/hello.txt")

# If file exists
filename = input("Specify file path: ")
if os.path.exists(filename):
    print("The file exists") 
else:
    print("The file does not exist")
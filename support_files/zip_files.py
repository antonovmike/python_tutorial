# ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True, compresslevel=None, *, strict_timestamps=True, metadata_encoding=None)

"""
Create zip file:

from zipfile import ZipFile
myzip = ZipFile("some.zip", "w")
myzip.close()

OR

with ZipFile("some.zip", "w") as myzip:
    pass
"""

# write(filename, arcname=None, compress_type=None, compresslevel=None)

"""
NO COMPRESSION
- Rewrite content:

from zipfile import ZipFile

with ZipFile("some.zip", "w") as myzip:
    myzip.write("hello.txt")

- Append content:

from zipfile import ZipFile

with ZipFile("metanit.zip", "a") as myzip:
    myzip.write("hello2.txt")
    myzip.write("forest.jpg")

- File name warning:

with ZipFile("metanit.zip", "a") as myzip:
    myzip.write("hello.txt", "hello1.txt")
    myzip.write("hello.txt", "hello2.txt")
    myzip.write("hello.txt", "hello3.txt")
"""

"""
COMPRESSION

from zipfile import ZipFile, ZIP_DEFLATED

with ZipFile("some.zip", "w", compression=ZIP_DEFLATED, compresslevel=3) as myzip:
    myzip.write("hello.txt")
"""

"""
Get file info:

from zipfile import ZipFile

with ZipFile("some.zip", "a") as myzip:
    print(myzip.infolist())

Get files info:

from zipfile import ZipFile
 
with ZipFile("some.zip", "r") as myzip:
    for item in myzip.infolist():
        print(f"File Name: {item.filename} Date: {item.date_time} Size: {item.file_size}")
"""

"""
Check if an archive contents a folder:

from zipfile import ZipFile
 
with ZipFile("some.zip", "r") as myzip:
    for item in myzip.infolist():
        if(item.is_dir()):  
            print(f"Folder: {item.filename}")
        else:  
            print(f"File: {item.filename}")
"""
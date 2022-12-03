FILENAME = "messages.txt"
messages = list()

for i in range(4):
    message = input("Enter a line " + str(i+1) + ": ")
    messages.append(message + "\n")


with open(FILENAME, "a") as file:
    for message in messages:
    file.write(message)


print("Messages")
with open(FILENAME, "r") as file:
    for message in file:
        print(message, end="")


"""
with open("hello.txt", "w") as file:
    file.write("hello world")
    
with open("hello.txt", "a") as file:
    file.write("\ngood bye, world")
    
with open("hello.txt", "a") as hello_file:
    print("Hello, world", file=hello_file)
    
    
with open("hello.txt", "r") as file:
    for line in file:
        print(line, end="")

with open("hello.txt", "r") as file:
    str1 = file.readline()
    print(str1, end="")
    str2 = file.readline()
    print(str2)

with open("hello.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()

with open("hello.txt", "r") as file:
    content = file.read()
    print(content)
    
with open("hello.txt", "r") as file:
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    print(str1, end="")
    print(str2)

filename = "hello.txt"
with open(filename, encoding="utf8") as file:
    text = file.read()
"""
try:
    somefile = open("hello_1.txt", "w")
    try:
        somefile.write("hello world 1")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)
    
with open("hello_2.txt", "w") as somefile:
    somefile.write("hello world 2")
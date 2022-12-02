try:
    number = int(input("Enter a number: "))
    print("Your number is:", number)
except:
    print("Conversion failed")

finally:
    print("Unit try has completed the execution")
print("Programm terminated")

try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a number: "))
    print(number1, "/", number2, "=", number1/number2)

except ValueError:
    print("Conversion failed")

except ZeroDivisionError:
    print("Attempt to divide a number by zero")
except BaseException:
    print("General exception")

finally:
    print("Unit try has completed the execution")
print("Programm terminated")

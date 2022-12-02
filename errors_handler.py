try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a number: "))
    print(number1, "/", number2, "=", number1/number2)

except ValueError as e:
    print("(Value Error) Invalid number:", e)

except ZeroDivisionError:
    print("(Zero Division Error) Attempt to divide a number by zero")

except BaseException:
    print("(Base Exception) General exception")

finally:
    print("Unit try has completed the execution")
print("Programm terminated")

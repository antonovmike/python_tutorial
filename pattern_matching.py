# Python 3.8 does not support pattern matching?
# https://peps.python.org/pep-0636/

def print_hello(language):
    match language:
        case "russian":
            print("Привет")
        case "english":
            print("Hello")
        case "german":
            print("Hallo")
        case _:
            print("Undefined")
 
 
print_hello("english")      # Hello
print_hello("spanish")      # Undefined

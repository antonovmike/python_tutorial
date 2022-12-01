class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1
# self.age - an atribute
# self.__age - a private atribute
    def set_age(self, age):
        if 1 < age < 120:
            self.__age = age
        else:
            print("Invalid age")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.name}\tAge: {self.age}")

alice = Person("Alice")
alice.name = "Zombie hunter"
alice.age = 30
alice.display_info()

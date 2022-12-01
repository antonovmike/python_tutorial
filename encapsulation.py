class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1
# self.age - an atribute
# self.__age - a private atribute
    @property
    def age(self):
        return self.__age
        
    @age.setter
    def age(self, age):
        if 1 < age < 120:
            self.__age = age
        else:
            print("Invalid age")

    @property
    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}\tAge: {self.__age}")

alice = Person("Alice")
alice.name = "Zombie hunter"
alice.age = 30
alice.display_info()


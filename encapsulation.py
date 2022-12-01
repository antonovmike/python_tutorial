class Person:
    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"Name: {self.name}\tAge: {self.age}")

alice = Person("Alice")
alice.name = "Zombie hunter"
alice.age = 30
alice.display_info()

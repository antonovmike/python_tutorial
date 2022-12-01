class Person:
    type = "Person"
    description = "Describes a person"
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

    def do_nothing(self):
        print(f"{self.__name} does nothing")

alice = Person("Alice")
alice.name = "Zombie hunter"
alice.age = 30
alice.display_info()



class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f"Company: {self.company}")

    def work(self):
        print(f"{self.get_name} works")

wesker = Employee("Alex Wesker", "Umbrella")
print(wesker.get_name)
wesker.display_info()
wesker.work()


def act(person):
    if isinstance(person, Employee):
        person.work()
    elif isinstance(person, Person):
        person.do_nothing()

act(alice)
act(wesker)


print(Person.description)
Person.type = "Class Person"
print(Person.type)

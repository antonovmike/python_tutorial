# Tuples are immutable

alice = ("Alice", 30)
print(alice)
wesker = "Wesker", 35
print(wesker)

some_list = ["Fruit", 70, "Peace"]
some_tuple = tuple(some_list)
print(some_tuple[2])
print("Tuple lenght", len(some_tuple))

name, age, company, position = ("Mike", 39, "Canonical", "software developer")
print(name)
print(age)
print(position)
print(company)

mike = ("Mike", 39, "Canonical", "software developer")
print(mike[:3]) # ('Mike', 39, 'Canonical')
print(mike[1:3]) # (39, 'Canonical')


def get_user():
    name = "Maria Salomea Skłodowska-Curie"
    age = 66
    company = "Université de Paris"
    return name, age, company


user = get_user()
print(user) # ("Tom", 37, "Google")


def print_person(name, age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")

pierre = ("Pierre Curie", 46)
print_person(*pierre, "la Sorbonne")


iterate_tuple = ("one", 2, "three")

for item in iterate_tuple:
    print(item)

i = 0
while i < len(iterate_tuple):
    print(iterate_tuple[i])
    i += 1


user = ("Mike", 39, "unemployed")
name = "Mike"
if name in user:
    print("User's name is", name)
else:
    print("User has another name")

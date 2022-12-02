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

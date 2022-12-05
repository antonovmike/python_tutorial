import csv


FILENAME = "users.csv"


users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]


with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)


with open(FILENAME, "a", newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)


with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1])


# csv.DictWriter() and csv.DictReader()

FILENAME = "users_dict.csv"


users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]

with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    # Write few lines
    writer.writerows(users)

    user = {"name" : "Sam", "age": 41}
    # Write 1 line
    writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "-", row["age"])
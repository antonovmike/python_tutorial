# dictionary = { key0: value_a, key1: value_b }
# Examples of dictionaries

uzbekistani_writers = {
    "+111111111": "Alisher Navoiy",
    "+222222222": "Muhammad Yusuf Bayoniy",
    "+333333333": "Abdulla Qodiriy"
}

print(uzbekistani_writers["+111111111"])

uzbekistani_writers["+222222222"] = "Muhammad Yusuf Bayoniy"
print(uzbekistani_writers["+222222222"])
# Add new writer
uzbekistani_writers["+444444444"] = "Munis Shermuhammad"

key = "+444444444"
if key in uzbekistani_writers:
    writer = uzbekistani_writers[key]
    print(writer)
else:
    print("Writer not found")

# Copy
uzbekistani_writers_1 = uzbekistani_writers.copy()

# Remove writer
if key in uzbekistani_writers:
    del uzbekistani_writers["+444444444"]
    print(f"Writer with key", key, "removed")
else:
    print("Writer not found")

removed_writer_2 = uzbekistani_writers_1.pop("+333333333")
removed_writer_1 = uzbekistani_writers_1.pop("+222222222", "Unknown Writer")

# Combine
uzbekistani_writers_1.update(uzbekistani_writers)

# Iterate
print(uzbekistani_writers_1)
for key in uzbekistani_writers_1:
    print(f"Id: {key} Writer: {uzbekistani_writers_1[key]}")

print(uzbekistani_writers)
for key, value in uzbekistani_writers.items():
    print(f"Id: {key} Writer: {value}")
    

# Remove all elements
uzbekistani_writers.clear()


users_list = [
    ["+111111111", "Alisher Navoiy"],
    ["+222222222", "Muhammad Yusuf Bayoniy"],
    ["+333333333", "Abdulla Qodiriy"]
]
users_dict = dict(users_list)
print(users_dict)


users_tuple = (
    ("+111111111", "Alisher Navoiy"),
    ("+222222222", "Muhammad Yusuf Bayoniy"),
    ("+333333333", "Abdulla Qodiriy")
)
users_dict = dict(users_tuple)
print(users_dict)

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:
    
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0")
                
    except ValueError:
        print("Your input is not a number")


user_input = ""
while user_input != "exit":
    user_input = input("Enter number of day and conversion unit\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()


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

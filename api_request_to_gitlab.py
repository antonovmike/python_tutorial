import requests

"""
Does not work if you use python command in terminal:

ModuleNotFoundError: No module named 'requests'

pip install requests
Requirement already satisfied: requests in /usr/lib/python3/dist-packages (2.22.0)

ModuleNotFoundError: No module named 'requests'

Use python3
"""

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
# print(response.text)
# print(response.json())
# print(response.json()[0])

my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['web_url']}\n")

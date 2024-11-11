import json

# Data to write to the JSON file
data = {
    "employees": [
        {"name": "Aneth", "age": 20, "city": "Nayarit"},
        {"name": "Vivian", "age": 25, "city": "Chihuahua"},
        {"name": "Carlos", "age": 15, "city": "Lerma"}
    ]
}

# Create and write data to the JSON file
with open("employees.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file 'employees.json' created successfully.")

import json

# Read the JSON file
with open("employees.json", "r") as file:
    data = json.load(file)
    print(data)
import json

# Read the existing JSON file
with open("employees.json", "r") as file:
    data = json.load(file)

# New entry to add
new_employee = {"name": "David", "age": 28, "city": "San Francisco"}

# Add the new employee to the data
data["employees"].append(new_employee)

# Write the updated data back to the JSON file
with open("employees.json", "w") as file:
    json.dump(data, file, indent=4)

print("New employee added to the JSON file 'employees.json'.")
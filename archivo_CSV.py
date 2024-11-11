import csv

# Data to write to the CSV
data = [
    ["Name", "Age", "City"],
    ["Aneth", 20, "Nayarit"],
    ["Vivian", 25, "Chihuahua"],
    ["Carlos", 15, "Lerma"]
]

# Create and write data to the CSV file
with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file 'people.csv' created successfully.")

import csv

# Read the CSV file
with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
import csv

# New row to add
new_row = ["David", 28, "San Francisco"]

# Open the CSV file in append mode and write the new row
with open("people.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_row)

print("New row added to the CSV file 'people.csv'.")
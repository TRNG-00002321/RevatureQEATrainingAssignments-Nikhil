import json
import os.path

with open("example.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1, line2)

with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("example.txt", "r") as file:
    while chunk := file.read(1024):
        print(chunk)

path = os.path.join("example.txt")
with open(path, "r") as file:
    print(file.read())

with open("output.txt", "w") as file:
    file.write("THis is the first line. \n")
    file.write("This will overwrite any existing content. \n")

with open("output.txt", "a") as file:
    file.write("This line is appended.\n")

try:
    with open("newfile.txt", "x") as file:
        file.write("This file was just created")
except FileExistsError:
    print("File already exists")

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("multilines.txt", "w") as  file:
    file.writelines(lines)

name = "Alice"
score = 95
with open("report.txt", "w") as file:
    file.write(f"student: {name}\nScore: {score}\n")

data = bytes([120, 3, 255, 0, 100])
with open("binary.dat", "wb") as file:
    file.write(data)

my_data = {
    "name" : "Alice",
    "age": 30,
    "city": "New York",
    "isStudent": False,
    "courses": ["Math", "Science"]
}
with open('data.json', 'w') as f:
    json.dump(my_data, f, indent=4)

with open('data.json', 'r') as f:
    json.load(f)
print(data)


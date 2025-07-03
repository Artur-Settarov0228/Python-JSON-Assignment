import json
import os

filename = "students.json"

if not os.path.exists(filename):
    with open(filename, 'w') as json_file:
        json.dump([] , json_file, indent=4)
    print(f" {filename} , file yaratildi . ")
else:
    print(f"{filename} mavjut ekan.")

with open('students.json' , 'r') as json_file_r:
    students = json.load(json_file_r)
    
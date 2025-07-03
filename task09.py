import json

with open('students.json' ,'r') as json_file:
    students = json.load(json_file)

total = len(students)

print(f"Talabalarning umimiy soni {total} ta")
import json

with open('students.json' , 'r') as json_file:
    students = json.load(json_file)

sorted_age = sorted(students , key=lambda x : int(x['age']), reverse=True)

for student in sorted_age:
    print(f"{student['name']} , {student['surname']}, {student['age']} yosh")


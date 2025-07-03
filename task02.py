import json


with open('students.json','r') as jsonfile:
    students = json.load(jsonfile)


for student in students:
    print(f"{student['name']} -- {student['age']} yoshda")    
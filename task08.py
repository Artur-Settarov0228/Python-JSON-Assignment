import json

with open('students.json' ,'r') as json_file:
    students = json.load(json_file)

age = [int(student['age']) for student in students]    

if age:
    max_age = max(age)
    print(f"max age , {max_age}")

else:
    print("error")
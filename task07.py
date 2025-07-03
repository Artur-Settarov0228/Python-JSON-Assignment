import json

with open('students.json','r') as json_file:
    students = json.load(json_file) 


ages = [int(student['age']) for student in students]

if ages:
    average = sum(ages) / len(ages)
    print(f"ortacha yosh , {average}")
else:
    print("error")
import json
new_list_students ={
    "name": "Shahzoda", 
    "surname": "Nazarova",
    "age": 22
    } 
with open('students.json','r') as json_file:
    students = json.load(json_file)


students.append(new_list_students)

with open('students.json' ,'w') as jsonfile:
    json.dump(students, jsonfile , indent=2)
    
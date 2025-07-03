import json
with open('students.json','r') as jsonfile:
    students = json.load(jsonfile)


name = input("ism kiriiting :")
surname = input('familayni kiriitng :')
age = input("yoshni kiriting :")

students.append({"name":name , "surname":surname, "age" : age})

with open('students.json' , 'w') as jsonfile:
    json.dump(students, jsonfile, indent=4)
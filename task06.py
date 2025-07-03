import json
import csv

with open('students.json' , 'r') as json_file:
    students = json.load(json_file)


with open('students.csv', 'w') as csv_file:
    fieldnames = [ 'name' , 'surname' , 'age']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for student in students :
        writer.writerow(student)

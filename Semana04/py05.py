student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)
print(student['courses'])
print(student.get('phone'))

for key, value in student.items():
    print(key, value)
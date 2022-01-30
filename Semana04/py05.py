student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)
print(student['courses'])
print(student.get('phone'))
del student['age']
print(len(student))
print(len(student))
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)
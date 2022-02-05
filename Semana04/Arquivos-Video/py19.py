
li = [10, 12, 13, 4, 25, 46, 57, 18, 9, 10]
s_li = sorted(li)
print(s_li)
li.sort()
print(li)
tup = (1, 12, 41, 51, 6, 7, 90)
s_tup = sorted(tup)
di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Windows'}
s_di = sorted(di)
print(s_di)
print(s_tup)

from operator import attrgetter

class Empregador():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Empregador('Jose', 18, 30000)
e2 = Empregador('Maria', 30, 330000)
e3 = Empregador('Jorge', 17, 130000)

empregados = [e1, e2, e3]


def e_sort(emp):
    return emp.salary


s_employes = sorted(empregados, key=attrgetter('age'))

print(s_employes)

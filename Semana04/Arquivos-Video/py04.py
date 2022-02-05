
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)



tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art' # Tupla nao aceita mudanças

print(tuple_1)
print(tuple_2)


cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)



empty_list = []
empty_list = list()


empty_tuple = ()
empty_tuple = tuple()


empty_set = {} # Não está certo por ser um dicionário
empty_set = set()
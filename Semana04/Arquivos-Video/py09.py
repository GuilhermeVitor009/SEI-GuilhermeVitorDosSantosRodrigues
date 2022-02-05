from cgi import test
import module09
import sys

sys.path.append('/Users/pexim/Desktop/My-Modules')

courses = ['History', 'Math', 'Physics', 'CompSci']

index = module09.find_index(courses, 'Math')

print(index)
print(test)
print(sys.path)
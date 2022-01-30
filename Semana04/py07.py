nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found')
        break
print(num)
x = 0
for noms in nums:
    for letter in 'abc':
        print(noms, letter)
        
while True:
    if x == 5:
        break
    print(x)
    x += 1
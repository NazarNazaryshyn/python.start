# Task 1

str = 'bbbbAFAFAbbBB'
c = 0
for i in str:
    if i == 'b':
        c += 1
print(c)

# Task 2
#
name = input('Enter your name: ')

for i in name:
    if i.isdigit():
        print('Error')
        break
    elif i == name[0] and i.islower():
        print('Error')
        break
    elif not i == name[0] and i.isupper():
        print('Error')
        print(i)
        break

# Task 3

a = input('Enter any string: ')

summ = 0
for j in a:
    summ += ord(j)
print(summ)
#
# Task 4

import math

k = 2
for i in range(10):
    print(f'{math.pi:.{k}f}')
    k += 1

# Task 5

a = input('Enter any string: ')
lis = a.split()
print(lis)
b = lis[0]
for i in lis:
    if len(i) > len(b):
        b = i

print(b)

# Extra task 1

x = input('Enter any string: ')

i = 0
n = ''
while i < len(x):
    if i == 0:
        n += x[i]
    elif x[i] in n:
        break
    else:
        n += x[i]
    i += 1
print(n)

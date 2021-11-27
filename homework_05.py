# Task 1

for i in range(100):
    if not i % 7:
        print(i)

# Task 2

n = int(input('Enter a number from 5 to 15:'))
i = 0
res = 1
if 4 < n < 16:
    while (i := i + 1) <= n:
        res *= i
    i += 1
print(res)

# Task 3

i = 0
while (i := i + 1) <= 10:
    print(5,'x', i,'=', 5*i)

# Task 4

x = int(input('Enter the width of rectangle:'))
y = int(input('Enter the height of rectangle:'))
i = 0
while i < x:
    if i == x - 1:
        print('*')
        i += 1
    else:
        print('*', end='')
        i += 1
i = 0
while i < y - 2:
    print('*',' ' * (x - 4),'*')
    i += 1
    if i == y - 2:
        print('*' * x)

# Task 5

a = [0,5,2,4,,17,3,19]
res = 0
for i in a:
    if i % 2:
        res += i
print(res)


# Task 7

import random
lis = []
res = 0
count = 0
for i in range(12):
    lis.append(random.randint(7500,15000))
print(lis)
for j in lis:
    res += j
    count += 1
print('Average salary: ',res/count)

# Task 8

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
summ = 0
for i in matrix:
    for j in i:
        summ += j
print(summ)

# Task 11

x = list(input('Enter a list'))
print(x)
x.reverse()
print(x)

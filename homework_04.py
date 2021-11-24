# Task 1

x = input('Enter four-digit number:')
y = int(x[0]) + int(x[1])
z = int(x[2]) + int(x[3])
if y == z:
    print('You are lucky')
else:
    print(':(')

# Task 2

num = input('Enter six-digit number:')

a = list(num[:3])
b = list(num[3:])

if a[0] == b[-1] and a[1] == b[-2] and a[2] == b[-3]:
    print('You are lucky')
else:
    print(':(')

# Task 3

x = float(input('Enter x:'))
y = float(input('Enter y:'))

if x**2 + y**2 <= 4**2:
    print('Inside the circle')
else:
    print('Outside the circle')
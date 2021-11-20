x = int(input('Enter the value of x:'))
y = int(input('Enter the value of y:'))
z = int(input('Enter the value of z:'))
# Task 1

if x%2:
    print('x is odd')
else:
    print('x is even')

if x%20:
    print('x is not a multiple of 20')
else:
    print('x is a multiple of 20')

# Task 2

if x > 0 and y > 0:
    print('x and y are both positive')
elif x < 0 and y < 0:
    print('x and y are both negative')
else:
    print('x and y have the different signs')

# Task 3

if x == y and x == z:
    print('All three names are bound to eqaul values')
elif x != y and x != z and y != z:
    print('All three names have the different values')
else:
    print('Two variables have the same value')


# Task 1

n1 = int(input('Enter first num:'))
n2 = int(input('Enter second num:'))
n3 = int(input('Enter third num:'))
n4 = int(input('Enter fourth num:'))

if n1 > n2 and n1 > n3 and n1 > n4:
    print('Max number is',n1)
elif n2 > n3 and n2 > n4:
    print('Max number is',n2)
elif n3 > n4:
    print('Max number is',n3)
else:
    print('Max number is',n4)


# Task 2

import math
apartment = int(input('Enter the number of your apartment:'))
if apartment > 144 or apartment <= -1:
    print('Error')
elif apartment > 108:
    entrance = 4
    floor = math.ceil((apartment - 36 * (entrance - 1)) / 4)
    print('Entrance -', entrance, 'floor -', floor)
elif apartment > 72:
    entrance = 3
    floor = math.ceil((apartment - 36 * (entrance - 1)) / 4)
    print('Entrance -', entrance, 'floor -', floor)
elif apartment > 36:
    entrance = 2
    floor = math.ceil((apartment - 36 * (entrance - 1)) / 4)
    print('Entrance -', entrance, 'floor -', floor)
else:
    entrance = 1
    floor = math.ceil(apartment / 4)
    print('Entrance -',entrance,'floor -',floor)

# Task 3

year = int(input('Enter a year:'))
if year % 4:
    print('365 days')
else:
    print('366 days')

# Task 4

a = int(input('Enter fist side:'))
b = int(input('Enter second side:'))
c = int(input('Enter third side:'))

if a + b > c and a + c > b and b + c > a:
    print('Triangle exists')
else:
    print('Triangle does not exist')

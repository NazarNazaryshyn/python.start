# Task 1

set_one = set(input('Enter any text: '))
set_two = set(input('Enter any text 2: '))

print(set_one & set_two)

# Task 2

import random
l_one = set ([x for x in range(100) if x % 3 == 0])
print(l_one)
l_two = set ([x for x in range(100) if x % 5 == 0])
print(l_two)

print(l_one & l_two)

# Extra task 2

dict = {
    'X':10,
    'V':5,
    'I':1
}

x = input('= ')
summ = 0
for i in x:
    summ += dict[i]
print(summ)


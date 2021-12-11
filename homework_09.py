# Task 1

def max_num(*a:list) -> int:
    """
    :param a: list
    :return: the highest value of the list
    """
    return max(a)

print(max_num(6,22,3,4,5))

# Task 2

def concatenation(a:int,b:int,c:str):
    """
    :param a: int
    :param b: int
    :param c: int
    :return: concatenate string
    """
    d = str(a + b)
    return c + d

print(concatenation(1,2,'text'))

# Task 3

def rectangle(a:int,b:int):
    """
    :param a: width of the rectangle
    :param b: height of the rectangle
    :return: rectangle
    """
    print('*' * a)
    i = 0
    while i < b - 2:
        print('*',' ' * (a - 4),'*')
        i += 1
    print('*' * a)

rectangle(10,4)

# Task 4

def find_num(a:list,b:int|str):
    """
    :param a:list 
    :param b:list item
    :return:index of the list item
    """
    for i in a:
        if i == b:
            return a.index(b)
    else:
        print(-1)
x = [1,2,3,4,5]
y = 10

print(find_num(x,y))

# Task 5

def get_length(a:str):
    """

    :param a: string
    :return: length of the string
    """
    return len(a.split(' '))

print(get_length('aafhafjq fqiofiaf qjkjfa fqjq9q jfoqfiqf, iqfoqif ,fqffqfq'))

# Extra task 1

def get_sequence(a):
    """

    :param a: list of sequence
    :return:  subsequent element of the list
    """
    if a[1] - a[0] == a[3] - a[2]:
        n = a[-1] + a[1] - a[0]
        return n
    elif a[1]/a[0] == a[2]/a[1]:
        n = a[-1] * (a[1]/a[0])
        return n
    elif a[1]-a[0] != a[2]-a[1]:
        n = a[-1] +  (a[-1] - a[-2]) + (a[2] - a[1]) - (a[1] - a[0])
        return n

b= [0,2,4,6,8,10,12]
print(get_sequence(b))
c= [1,4,7,10,13]
print(get_sequence(c))
d = [1,2,4,8,16,32]
print(get_sequence(d))
e = [1,3,9,27]
print(get_sequence(e))
f = [1,4,9,16,25]
print(get_sequence(f))








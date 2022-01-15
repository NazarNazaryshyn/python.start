# Task 1

def geom_subsequence(n: int, stop: int):
    """
    :param n: raise numbers to the n's power
    :param stop: limit of the geometric subsequence
    """
    i = 1
    while i <= stop:
        next_item = i * n
        i = next_item
        if next_item > stop:
            break
        else:
            yield next_item
    return


x = geom_subsequence(2, 100)
print('Geometric subsequence:')
for i in x:
    print(i)


# Task 2


def range_function(stop, start = 1, step = 1):
    """
    :param stop: limit of the sequence
    :param start: starting position
    :param step: step of the sequence
    """
    start = start
    while start <= stop:
        next_element = start + step
        start = next_element
        yield next_element
    return

y = range_function(50, step = 3)
print('Range fucntion:')
for item in y:
    print(item)


# Task 3

def prime_nums(stop: int):
    """
    :param stop: the limit of the sequence
    """
    for i in range(2, stop):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i


x = prime_nums(50)
print('Prime numbers:')
for item in x:
    print(item)


# Task 4


my_list = [x**2 for x in range(2, 20)]
print(f'List:\n{my_list}')
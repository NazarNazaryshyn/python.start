# Task 2


def factorial_memo(func):
    data = {}
    def internal(*args):
        if args in data:
            return data[args]
        new_value = func(*args)
        data[args] = new_value
        return new_value
    return internal



def factorial(n):
    """
    :param n: Takes an integer
    :return: Returns the factorial of n
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)



x = factorial_memo(factorial)

print(x(5))
print(x(5))


# Task 3


my_list = [1, 2, 3, 4, 5]

def function(func, lis):
    """
    :param func: Takes a function that makes some actions on each element of list as argument
    :param lis: Takes a list as argument
    :return: Returns the sum of elements in list
    """
    def wrapped():
        return sum(list(func(i) for i in lis))
    return wrapped()


def pow(x: int):
    """
    :param x: Takes as argument an integer
    :return: Returns the second power of an argument
    """
    return x ** 2


print(function(pow, my_list))



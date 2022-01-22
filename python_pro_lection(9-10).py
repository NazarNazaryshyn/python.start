import time


# Lection_9 | Task 1


class Decorator:
    count = 0

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        Decorator.count += 1
        return self.f(*args, **kwargs)


@Decorator
def add(x, y):
    return x + y

print(f'Add = {add(1,3)}')
print(f'Number of calls: {Decorator.count}')

print(f'Add = {add(1,3)}')
print(f'Number of calls: {Decorator.count}')

print(f'Add = {add(1,3)}')
print(f'Number of calls: {Decorator.count}')


# Lection_9 | Task 2


func_list = []

def reg_func(f):
    func_list.append(f)
    return f

@reg_func
def sub(a, b):
    return a - b

@reg_func
def div(a, b):
    return a / b

print(func_list)


# Lection_9 | Task 3


def func_1(func):
    def wrapper(*args, **kwargs):
        with open(f'{Student.name}.txt', 'w') as file:
            file.write(func(*args, **kwargs))
            return func(*args, **kwargs)
    return wrapper


class Student:

    name = 'Student'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @func_1
    def __str__(self):
        return f'Student {self.name} is {self.age} years old'


ex = Student('Mark', '25')

print(ex)


# Lection_9 | Task 4


def f_1(n = 1, folder = 'fibb_func'):
    def f_2(func):
        i = 0
        res = 0
        start_time = time.time()
        def wrapper(*args, **kwargs):
            nonlocal i, res
            while i < n:
                res += int(func(*args, **kwargs))
                i += 1
            finish_time = time.time()
            with open(f'{folder}.txt', 'w') as file:
                file.write(str(finish_time - start_time))
            return res
        return wrapper
    return f_2

@f_1(n = 2, folder='fibb_func')
def fibbonachi(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fibbonachi(n - 1) + fibbonachi(n - 2)



print(fibbonachi(40))


# Lection_10 | Task 1


class_list = []

def class_reg(func):
    class_list.append(func)
    return func


@class_reg
class Cls_dec:
    def __init__(self):
        pass


    def __call__(self, *args, **kwargs):
        pass

ex_1 = Cls_dec()

print(class_list)


# Lection_10 | Task 2


def str_decor(param):
    def decor(func):
        def wrapper(*args, **kwargs):
            return f'{param}{func(*args, **kwargs)}'
        return wrapper
    return decor


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @str_decor('text text text text ')
    def __str__(self):
        return f'{self.name} is {self.age} years old'


pers_ex = Person('Oleksandr', '29')
print(pers_ex)


# Lection_10 | Task 3


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqaure(self):
        return self.x * self.y * self.z

    @staticmethod
    def get_sqaure(b_1, b_2):
        if isinstance(b_1, Box) and isinstance(b_2, Box):
            return b_1.sqaure() + b_2.sqaure()


box_1 = Box(2,2,3)
box_2 = Box(3,4,5)

x = Box.get_sqaure(box_1, box_2)
print(x)

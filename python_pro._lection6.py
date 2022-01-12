import datetime
MAX_STUDENTS = 10

# Task 1


class Human:
    def __init__(self, date_of_birth: 'YYYY/MM/DD', sex, country):
        self.age = datetime.datetime.now().year - int(date_of_birth.split('/')[0])
        self.sex = sex
        self.country = country

    def __str__(self):
        return f'Age = {self.age}, sex = {self.sex}, country = {self.country}'


class Student(Human):
    def __init__(self, date_of_birth, sex, country, name):
        super().__init__(date_of_birth, sex, country)
        self.name = name

    def __str__(self):
        return f'Student {self.name}. {super().__str__()}'


class Group:
    def __init__(self, name_of_group,entrance_year, students=None):
        self.name_of_group = name_of_group
        self.entrance_year = entrance_year
        self.students = students or []


    def __getitem__(self, index):
        if isinstance(index, slice):
            if index.start < 0 or index.stop > len(self.students):
                raise IndexError
            else:
                res = []
                start = 0 if index.start == None else index.start
                stop = len(self.students) - 1 if index.stop == None else index.stop
                step = 1 if index.step == None else index.step
                for i in range(start, stop, step):
                    res.append(self.students[i])
                return res

        if isinstance(index, int):
            if index < len(self.students):
                return self.students[index]
            else:
                return IndexError
        return TypeError


    def add_student(self, student):
        if student in self.students:
            raise Exception('The student is already in group')
        elif len(self.students) < MAX_STUDENTS:
            self.students.append(student)
        else:
            raise LenError('The group full of students')

    def __iter__(self):
        return GroupIter(self.students)

    def __str__(self):
        res = '\n'.join(map(str, self.students))
        return f'{self.name_of_group}: {self.entrance_year}\n{res}'



class GroupIter:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self



class LenError(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

gr_1 = Group('Software engineering', '2014')


st_1 = Student('1995/12/12', 'female', 'Ukraine', 'Olga')
st_2 = Student('2001/12/12', 'male', 'Ukraine', 'Dmytro')
st_3= Student('1985/12/12', 'male', 'Ukraine', 'Petro')
st_4= Student('1967/12/12', 'female', 'Ukraine', 'Sofia')
st_5= Student('1999/12/12', 'male', 'Ukraine', 'Illya')


gr_1.add_student(st_1)
gr_1.add_student(st_2)
gr_1.add_student(st_3)
gr_1.add_student(st_4)
gr_1.add_student(st_5)

print(gr_1[0:5])


# Task 2


class Item:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def __str__(self):
        return f'Item - {self.name}, price - {self.price}$, size - {self.size}'

item_1 = Item('Ball','12.3', '30cm')
item_2 = Item('Shirt','15.99','70cm')
item_3 = Item('Coat','29.99','100cm')


class Customer:
    def __init__(self, name, lastname, middlename, age, phone):
        self.name = name
        self.lastname = lastname
        self.middlename = middlename
        self.age = age
        self.phone = phone

    def __str__(self):
        return f'{self.lastname} {self.name} {self.middlename} {self.age} years old, mobile phone - {self.phone}'

customer_1 = Customer('Vitaliy','Kuzmenko','Vitaliyovich','22','+380674525347')
customer_2 = Customer('Denis','Korsun','Illich','25','+380654323654')
customer_3 = Customer('Adnriy','Rudiy','Mukolayovich','34','+380983421696')


class Order:
    def __init__(self, customer, order, price ):
        self.customer_name = customer
        self.order_name = order
        self.order_price = price

    def __str__(self):
        return f'{self.order_name} ordered by {self.customer_name}, total price - {self.order_price}$'

class OrderBasket:
    def __init__(self):
        self.basket = []


    def add_item(self, item):
        self.basket.append(item)


    def __getitem__(self, item):
        if isinstance(item, slice):
            if item.start < 0 or item.stop > len(self.basket):
                return IndexError
            else:
                res = []
                start = 0 if item.start == None else item.start
                stop = len(self.basket) - 1 if item.stop == None else item.stop
                step = 1 if item.step == None else item.step
                for i in range(start, stop, step):
                    res.append(self.basket[i])
                return res
        if isinstance(item, int):
            if item < len(self.basket):
                return self.basket[item]
            else:
                return IndexError
        return TypeError


    def __iter__(self):
        return OrderIter(self.basket)

class OrderIter:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self

order_1 = Order(f'{customer_1.name} {customer_1.lastname}', item_2.name, item_2.price)
order_2 = Order(f'{customer_1.name} {customer_1.lastname}', item_2.name, item_2.price)
order_3 = Order(f'{customer_1.name} {customer_1.lastname}', item_2.name, item_2.price)

order_4 = Order(f'{customer_2.name} {customer_2.lastname}', item_1.name, item_1.price)
order_5 = Order(f'{customer_2.name} {customer_2.lastname}', item_1.name, item_1.price)


order_6 = Order(f'{customer_3.name} {customer_3.lastname}', item_3.name, item_3.price)

basket_1 = OrderBasket()

basket_1.add_item(order_1)
basket_1.add_item(order_2)
basket_1.add_item(order_3)





print(basket_1[1:3])
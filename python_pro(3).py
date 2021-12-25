import datetime
MAX_STUDENTS = 10
# Task 1


class Item:
    def __init__(self, price: (int, float, str)):
        if isinstance(price, (float, int)) and price < 0:
            raise TypeError
        elif isinstance(price, str) and not price.replace('.','').isdigit():
            raise TypeError

        self.price = price
    def __str__(self):
        return f'Price - {self.price}$'


# Task 2


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

    def add_student(self, student):
        if student in self.students:
            raise Exception('The student is already in group')
        elif len(self.students) < MAX_STUDENTS:
            self.students.append(student)
        else:
            raise LenError('The group full of students')

    def __str__(self):
        res = '\n'.join(map(str, self.students))
        return f'{self.name_of_group}: {self.entrance_year}\n{res}'


class LenError(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

gr_1 = Group('Software engineering', '2014')


st_1 = Student('1995/12/12', 'female', 'Ukraine', 'Olga')
st_2 = Student('2001/12/12', 'male', 'Ukraine', 'Dmytro')
st_3= Student('1085/12/12', 'male', 'Ukraine', 'Petro')


gr_1.add_student(st_1)
gr_1.add_student(st_2)
gr_1.add_student(st_3)











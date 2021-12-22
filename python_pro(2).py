class Human:
    def __init__(self, age, gender, country ):
        self.age = age
        self.gender = gender
        self.country = country

    def __str__(self):
        return f'Age = {self.age}, gender = {self.gender}, country = {self.country}'


class Student(Human):
    def __init__(self, age, gender, country, name, grade, faculty):
        super().__init__(age, gender, country)
        self.name = name
        self.grade = grade
        self.faculty = faculty
    def __str__(self):
        return f'Student {self.name} is a {self.grade}-year student of {self.faculty} faculty. {super().__str__()}'


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, x):
        for i in self.students:
            if i.name == x:
                print(i)

    def remove_student(self,student):
        self.students.remove(student)

    def __str__(self):
        a = ''
        for i in self.students:
            a += str(i) + '\n'
        return a


gr_1 = Group('Group_1')

st_1 = Student(19, 'male', 'Ukraine', 'Oleksandr', '2', 'IT')
gr_1.add_student(st_1)

st_2 = Student(17, 'female', 'Ukraine', 'Dasha', '1', 'Economic')
gr_1.add_student(st_2)

st_3 = Student(20, 'male', 'Ukraine', 'Petro', '4', 'IT')
gr_1.add_student(st_3)

st_4 = Student(18, 'female', 'Ukraine', 'Marina', '2', 'Law')
gr_1.add_student(st_4)

st_5 = Student(17, 'male', 'Ukraine', 'Ivan', '1', 'Agronomy')
gr_1.add_student(st_5)

gr_1.remove_student(st_1)

print(gr_1)

print(gr_1.find_student('Ivan'))









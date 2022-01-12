import math
from math import gcd
# Task 1


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def sqaure(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.sqaure() == other.sqaure()
        return TypeError

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.sqaure() + other.sqaure()
        return TypeError

    def mul_n(self, n):
        self.width *= n
        self.height *= n
        return self.width, self.height

    def __str__(self):
        return f'Width={self.width}\nHeight={self.height}'


rt_1 = Rectangle(5, 3)
rt_2 = Rectangle(1,15)

print(rt_1 +  rt_2)

rt_1.mul_n(3)

print(rt_1)


# Task 2


class CorrectFraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            print("You can't divide by zero")
            raise ValueError
        self.numerator = numerator
        self.denominator = denominator


    def __eq__(self, other):
        if isinstance(other, CorrectFraction):
            return self.numerator / self.denominator == other.numerator / other.denominator
        return TypeError

    def __add__(self, other):
        if isinstance(other, CorrectFraction):
            if self.denominator == other.denominator:
                return CorrectFraction(self.numerator + other.numerator, self.denominator)
            else:
                return CorrectFraction(self.numerator * other.denominator + other.numerator * self.denominator,self.denominator * other.denominator)

    def __sub__(self, other):
        if isinstance(other, CorrectFraction):
            if self.denominator == other.denominator:
                return CorrectFraction(self.numerator - other.numerator, self.denominator)
            else:
                return CorrectFraction(self.numerator * other.denominator - other.numerator * self.denominator,self.denominator * other.denominator)
    def __mul__(self, other):
        if isinstance(other, CorrectFraction):
            return CorrectFraction(self.numerator * other.numerator, self.denominator * other.denominator)


    def  __str__(self):
        return f'{self.numerator}/{self.denominator}'


fr_1 = CorrectFraction(2,6)
fr_2 = CorrectFraction(3,3)


print(fr_1 == fr_2)
print(fr_1 + fr_2)
print(fr_1 - fr_2)
print(fr_1 * fr_2)

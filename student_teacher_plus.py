#!/usr/bin/env python3
import sys
from collections import Counter
class Person(object):
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name

    def get_grade(self):
        return 0
class Student(Person):
    def __init__(self, name, branch, year, grade):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.grade = grade

    def get_details(self):
        return "{} student {} and {} year".format(self.name, self.branch, self.year)

    def get_grade(self):
        temp = Counter(self.grade).most_common(4)
        num1 = 0
        num2 = 0
        for item in temp:
            if item[0] != 'D':
                num1 += item[1]
            else:
                num2 += item[1]
        print("Pass: {}, Fail: {}".format(num1, num2))

class Teacher(Person):
    def __init__(self, name, classes, grade):
        Person.__init__(self, name)
        self.classes = classes
        self.grade = grade

    def get_details(self):
        return "{} teacher teached {}".format(self.name, ','.join(self.classes))

    def get_grade(self):
        temp = Counter(self.grade).most_common(4)
        s = []
        for i, j in temp:
            s.append("{}: {}".format(i, j))
        print(', '.join(s))

person1 = Person('tankoni')
#student1 = Student('tt', 'CSE', 2020)
#teacher1 = Teacher('kk', ['java', 'python'])

#print(person1.get_details())
#print(student1.get_details())
#print(teacher1.get_details())

if __name__ == '__main__':
    if sys.argv[1] == 'student':
        student1 = Student('tt', 'CSE', 2020, sys.argv[2])
        student1.get_grade()
    else:
        teacher1 = Teacher('kk', ['java', 'python'], sys.argv[2])
        teacher1.get_grade()

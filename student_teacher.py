#!/usr/bin/env python3
class Person(object):
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name

class Student(Person):
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        return "{} student {} and {} year".format(self.name, self.branch, self.year)

class Teacher(Person):
    def __init__(self, name, classes):
        Person.__init__(self, name)
        self.classes = classes

    def get_details(self):
        return "{} teacher teached {}".format(self.name, ','.join(self.classes))

person1 = Person('tankoni')
student1 = Student('tt', 'CSE', 2020)
teacher1 = Teacher('kk', ['java', 'python'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())


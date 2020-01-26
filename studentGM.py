#!/usr/bin/env python3
n = int(input("Please input the number of the students: "))
data = {}
subjects = ('a', 'b', 'c')
for i in range(0, n):
    name = input("Please input the {} name of student: ".format(i+1))
    points = []
    for x in subjects:
        points.append(int(input("Please input {}\'s point: ".format(x))))
    data[name] = points
for x,y in data.items():
    total = sum(y)
    print("{}\'s total points {}".format(x, total))
    if total < 100:
        print(x, "fialed :(")
    else:
        print(x, "passed :)")

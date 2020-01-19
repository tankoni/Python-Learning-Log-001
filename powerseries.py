#!/usr/bin/env python3
x = float(input("Please input a number between 0 and 1: "))
n = term = num = 1
result = 1.0
while n <= 100:
    term *= x / n
    result += term
    n += 1
    if term < 0.0001:
        break
print("times: {} and Sum: {}".format(n, result))

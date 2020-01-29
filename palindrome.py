#!/usr/bin/env python3
def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    s = input("Please input a string: ")
    if palindrome(s):
        print("is a palindrome")
    else:
        print("not a palindrome")

#!/usr/bin/env python3

class Account(object):

    def __init__(self, rate):   # ,__amt=0)
        self.__amt = 0          #__*** is a private property in python3
        self.rate = rate

    @property
    def amount(self):
        return self.__amt

    @property
    def cny(self):
        return self.__amt * self.rate

    @amount.setter
    def amount(self, value):
        if value < 0:
            print("no negative amount")
            #raise ValueError("the value error")
            return
        self.__amt = value      #set __amt>0

if __name__ == '__main__':
    acc = Account(rate=6.9)
    acc.amount = 20
    print("Dollar amount: ", acc.amount)
    print("CNY amount: ", acc.cny)
    acc.amount = -100
    print("Dollar amount: ", acc.amount)

#!/usr/bin/env python3
import sys

def Hours(minute):
    if minute < 0:
        raise Valueerror("the value cannot be negative")
    else:
        print("{} H, {} M".format(minute//60, minute%60))

try:
    Hours(int(sys.argv[1]))
except:
    print("Paramter Error")

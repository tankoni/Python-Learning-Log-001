#!/usr/bin/env python3
import sys
print("the sys.argv\'s first value", sys.argv[0])
print("the sys.argv\'s all value")
for i,x in enumerate(sys.argv):
    print(i, x)

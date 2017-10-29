# -*- coding: utf-8 -*-
a = int(raw_input("erste Zahl:"))
b = int(raw_input("zweite Zahl:"))
operation = raw_input("+ oder -:")

if operation == "+":
 print a + b
elif operation == "-":
 print a - b
elif operation == "*":
    print a * b
else:
    print "das geht so nicht"
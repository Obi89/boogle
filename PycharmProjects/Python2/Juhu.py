# -*- coding: utf-8 -*-

eingabe = int(raw_input("Highest number:"))
for zahl in range(0, eingabe+1):


    if zahl % 3 == 0 and zahl % 5 == 0:
        print str(zahl) + " Juhu! Jippi!"
    elif zahl % 3 == 0:
        print str(zahl) + " Juhu!"
    elif zahl % 5 == 0:
        print str(zahl) + " Jippi!"
    else:
        print zahl

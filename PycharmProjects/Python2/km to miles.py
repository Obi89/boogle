# -*- coding: utf-8 -*-
print "Hello! Welcome to the km to miles converter!"

while True:
    print "Please put in your Kilometers!"

    km = float(raw_input("Kilometer:"))

    miles = (km * 0.624)
    print str(km) + " km are " + str(miles) + " miles"

    print "Again?"

    answer = raw_input("yes or no?")

    if answer == "yes":
        print "Restart..."

    elif answer == "no":
        print "Goodbye..."
        break

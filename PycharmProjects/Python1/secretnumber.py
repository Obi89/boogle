# -*- coding: utf-8 -*-
import random

secret = (random.randint(1,10))

for hinweis in ["First Try","Second Try","Last Try"]:
    guess = int(raw_input("Guess the secret number (1-10):"))

    print hinweis

    if guess == secret:
        print "Congratulation! The secret number is: " + str(secret)
        break
    elif guess > secret:
        print "Your guess is not correct... try something smaller"
    elif guess < secret:
        print "Your guess is not correct... try something bigger"




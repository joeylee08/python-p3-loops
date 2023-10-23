#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
    print("Happy New Year!")
    pass

def square_integers(int_list):
    return [num * num for num in int_list]
    pass

def fizzbuzz():
    for i in range(100):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
    pass

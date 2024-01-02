#!/usr/bin/python3
for number in range(0, 10):
    for numero in range(number + 1, 10):
        if number == 8 and numero == 9:
            print("{}{}".format(number, numero))
        else:
            print("{}{}".format(number, numero), end=", ")

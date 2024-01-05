#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for d in my_string:
        if d is not 'c' and d is not 'C':
            new_str += d
    return (new_str)
## return my_string.translate({ord(c): None for c in "cC"})

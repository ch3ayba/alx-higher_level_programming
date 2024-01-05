#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ilist = my_list[:]
    for counter, d in enumerate(my_list):
        if d % 2 == 0:
            ilist[counter] = True
        else:
            ilist[counter] = False
    return(ilist)

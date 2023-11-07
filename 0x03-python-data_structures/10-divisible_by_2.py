#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listlen = len(my_list)
    if listlen == 0:
        return None
    multiples = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return multiples

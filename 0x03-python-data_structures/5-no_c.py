#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for i in range(len(my_string)):
        if i != 'c' and i != 'C':
            new_str += i
    return(new_str)

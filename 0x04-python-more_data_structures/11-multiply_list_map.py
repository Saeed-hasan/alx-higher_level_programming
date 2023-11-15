#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    tmp = []
    tmp.append(list(map(lambda x: x*number, my_list)))
    return tmp

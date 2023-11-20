#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    prints a list of anything, but only prints the integers
    Returns the amount of integers printed
    """
    result = 0
    for i in range(x):
        try:
            print(f"my_list=[i]", end="")
            result += 1
        except IndexError:
            break
    print()
    return result

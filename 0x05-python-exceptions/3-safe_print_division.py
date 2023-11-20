#!/usr/bin/python3
def safe_print_division(a, b):
    try: 
        x = a / b
    except (ZeroDivisionError, FloatingPointError, TypeError):
        x = None
    finally:
        print("Inside result:{}".format(res))
    return (x)

#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        print("Inside result: {}".format(result))
    except ZeroDivisionError:
        result = None
        print("Inside result: None")
        return result
    finally:
        return result

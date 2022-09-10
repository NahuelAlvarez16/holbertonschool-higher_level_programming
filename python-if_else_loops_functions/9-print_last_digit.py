#!/usr/bin/python3
def print_last_digit(number):
    last_number = -(-number % 10) if number < 0 else number % 10
    print("{:d}".format(last_number))
    return last_number

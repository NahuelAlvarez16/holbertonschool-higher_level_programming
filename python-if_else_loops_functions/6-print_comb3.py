#!/usr/bin/python3
for dozen in range(0, 9):
    for unit in range(dozen + 1, 10):
        print("{:d}{:d}".format(dozen, unit), end="")
        print("\n" if dozen == 8 and unit == 9 else ", ", end="")

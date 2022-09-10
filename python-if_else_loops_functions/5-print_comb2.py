#!/usr/bin/python3
for c in range(0, 99):
    print(("0" if c < 10 else "") + "{:d}".format(c), end=", ")
print("99")

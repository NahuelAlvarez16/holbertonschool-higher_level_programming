#!/usr/bin/python3
ignored_characters = [101, 113]
for c in range(97, 123):
    if c not in ignored_characters:
        print("{:c}".format(c), end="")

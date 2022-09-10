#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("0 argument.")
    else:
        print(f"{argc - 1}" + " argument" + ("s" if argc > 2 else ""))
        for idx, arg in enumerate(sys.argv):
            if idx > 0:
                print("{}: {}".format(idx, arg))

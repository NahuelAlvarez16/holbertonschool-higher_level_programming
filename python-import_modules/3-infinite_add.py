#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    argc = len(sys.argv)
    if argc == 1:
        print("0")
        quit()
    else:
        for idx, arg in enumerate(sys.argv):
            if idx > 0:
                result += int(arg)
    print("{}".format(result))

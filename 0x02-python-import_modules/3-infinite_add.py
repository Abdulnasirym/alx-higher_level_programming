#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    count = 0
    if arg == 1:
        print("0")
    elif arg > 1:
        for i in range(1, arg):
            count = count + int(sys.argv[i])
        print("{}".format(count))

#!/usr/bin/python3
start = ord('a')
stop = ord('z') + 1
for i in range(start, stop):
    print("{:c}".format(i), end='')
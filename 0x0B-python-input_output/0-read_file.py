#!/usr/bin/python3

def read_file(filename=""):
    with open (filename, encoding='utf-8') as f:
        f_content = f.read()
        print(f_content, end="")

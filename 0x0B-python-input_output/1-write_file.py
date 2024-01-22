#!/usr/bin/python3
"""Defines a function taht writes to a file"""

def write_file(filename="", text=""):
    """write a content to a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        f_content = f.write(text)
        print(f_content, end="")

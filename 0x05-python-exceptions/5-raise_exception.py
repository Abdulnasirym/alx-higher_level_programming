#!/usr/bin/pyhton3
def raise_exception():
    class CustomError(Exception):
        raise TypeError

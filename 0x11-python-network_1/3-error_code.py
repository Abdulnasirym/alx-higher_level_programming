#!/usr/bin/python3
""" Sends a request
    to the URL
"""


if __name__=="__main__":
    from urllib import request, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)


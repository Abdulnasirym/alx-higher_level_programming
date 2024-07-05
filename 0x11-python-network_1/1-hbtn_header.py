#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL """
import urllib.request
import sys


if __name__=="__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get('X-Request-Id'))

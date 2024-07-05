#!/usr/bin/python3
"""Takes in URL and display the value of a variable X-request-Id."""
import requests
import sys


if __name__=="__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))

#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL """

import urllib.request
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as resp:
        output = resp.headers.get('X-Request-Id')
        if output:
            print(output)
except urllib.error.URLError as e:
    print("Error")

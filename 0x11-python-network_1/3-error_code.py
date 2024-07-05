#!/usr/bin/python3
""" Sends a request to the URL"""
import urllib.request
import urllib.error
import sys


url = sys.argv[1]

if __name__=="__main__":
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code )

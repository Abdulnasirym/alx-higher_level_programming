#!/usr/bin/python3
""" ends a request to the URL and displays the body of the response. """
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if (response.status_code >= 400):
g       print("Error code: ", response.status_code)

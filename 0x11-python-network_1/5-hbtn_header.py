#!/usr/bin/python3
""" Takes in URL and display thevalue of a variable X-request-Id."""
import requests
import sys


r = requests.get(sys.argv[1])
print(r.headers['X-Request-Id'])

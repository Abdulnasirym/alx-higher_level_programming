#!/usr/bin/python3
""" fetches a url """
import requests


r = requests.get('https://alx-intranet.hbtn.io/status', auth=('user', 'pass'))
print("Body response:")
print("\t- type: {}".format(type(r)))
print("\t- content: {}".format(r))

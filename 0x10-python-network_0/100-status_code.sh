#!/bin/bash
#Sends request to a URL
curl -sILw "%{http_code}" "$1" 

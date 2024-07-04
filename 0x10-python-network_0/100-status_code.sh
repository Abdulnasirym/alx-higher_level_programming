#!/bin/bash
#Sends request to a URL
curl -so /dev/null -w "%{http_code}" "$1" 

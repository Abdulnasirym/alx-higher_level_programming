#!/bin/bash
#Sends request to a URL
curl -sIw "%{http_code}" "$1" 

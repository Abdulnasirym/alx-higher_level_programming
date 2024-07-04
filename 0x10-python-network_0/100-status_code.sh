#!/bin/bash
#Sends request to a URL
curl -sIL "$1" | grep "HTTP" | cut -d " " -f 2 

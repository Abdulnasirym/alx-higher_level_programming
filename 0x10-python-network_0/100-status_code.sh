#!/bin/bash
#Sends request to a URL
curl -sI "$1" | grep "HTTP" | cut -d " " -f 2 

#!/bin/bash
#Sends a JSON POST request to URL
curl -sX POST -H "Content-Type: application/json" -d "$2" "$1" 

#!/usr/bin/bash

if [ $# -ne 1 ]; then
	echo "Usage: $0 URL"
	exit 1
fi

url=$1

response=$(curl -sI "$url")
content_length=$(echo "$response" | grep -i 'content-length' | awk '{print $2}' | tr -d '\r')

if [ -z "$content_length" ]; then
	content_length=$(curl -s "$url" | wc -c)
fi

echo "Size of the body of the response: $content_length bytes"

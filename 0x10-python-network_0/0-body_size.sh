#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes.

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send a request to the URL and measure the size of the response body
response=$(curl -sI $URL | grep -i content-length | awk '{print $2}')
echo "Size of the response body: ${response} bytes"

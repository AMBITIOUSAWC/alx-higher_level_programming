#!/bin/bash
# Write a Bash script that sends a request to a URL passed as an argument,
# and displays only the status code of the response.

# Check if argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request with curl and capture the status code
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Display the status code
echo "Status code of $1: $status_code"

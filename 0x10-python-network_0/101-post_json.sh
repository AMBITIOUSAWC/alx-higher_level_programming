#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument and displays the body of the response.
# The JSON data is read from a file passed as the second argument.
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"


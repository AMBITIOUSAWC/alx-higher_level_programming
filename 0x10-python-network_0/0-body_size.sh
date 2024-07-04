#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes.
curl -S "$1" | WC -C

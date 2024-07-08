#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with email as a parameter.
    Prints the decoded body of the response.

    Args:
    - url (str): The URL to send the POST request to.
    - email (str): The email parameter to include in the POST request.
    """
    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    try:
        # Send a POST request with the email parameter
        with urllib.request.urlopen(url, data=data) as response:
            # Read and print the body of the response
            body = response.read().decode('utf-8')
            print("Response body:", body)
    except urllib.error.URLError as e:
        print(f"Error sending POST request: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)

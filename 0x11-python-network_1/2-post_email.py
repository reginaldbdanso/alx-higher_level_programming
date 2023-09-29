#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    # Get the url from the command line
    url = sys.argv[1]
    # Get the email from the command line
    email = sys.argv[2]
    # Encode the email
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    # Send the request
    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')
        print(body)

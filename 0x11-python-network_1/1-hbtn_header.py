#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    # Get the url from the command line
    url = sys.argv[1]
    # Send a request to the URL and get the response
    with urllib.request.urlopen(url) as response:
        # Get the header of the response
        header = response.info()
        # Print the value of the X-Request-Id variable found in the header
        print(header.get('X-Request-Id'))

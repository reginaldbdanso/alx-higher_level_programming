#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    # Get the url from the command line
    url = sys.argv[1]
    # Send the request and get the response
    response = requests.get(url)
    # Print the X-Request-Id header
    print(response.headers.get('X-Request-Id'))

#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8), while
managing the error.
"""
import requests
import sys


if __name__ == "__main__":
    # Get the url from the command line
    url = sys.argv[1]
    try:
        # Send the request and get the response
        response = requests.get(url)
        print(response.read().decode('utf-8'))
    # Manage the error
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")

#!/usr/bin/python3
"""This module fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    # Get the url from the command line
    url = 'https://alx-intranet.hbtn.io/status'
    # Send a request to the URL using urllib
    with urllib.request.urlopen(url) as response:
        # Get the body of the response
        html = response.read()
        # Print the body of the response
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")

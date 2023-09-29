#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    # Get the url from the command line
    url = 'https://alx-intranet.hbtn.io/status'
    # Send the request and get the response
    response = requests.get(url)
    # Print the response
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")

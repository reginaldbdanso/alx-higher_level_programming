#!/usr/bin/python3
"""Takes in a URL and an email address, sends a POST request to the
 passed URL with the email as a parameter, and displays the body of the response
 ."""
import requests
import sys


if __name__ == "__main__":
    # Get the url from the command line
    url = sys.argv[1]
    # Get the email from the command line
    email = sys.argv[2]
    # store the email in a dictionary
    data = {'email': email}
    # Send the request and get the response
    response = requests.post(url, data=data)
    # Print the response body
    print(response.text)

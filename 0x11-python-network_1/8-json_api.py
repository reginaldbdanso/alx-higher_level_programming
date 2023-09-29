#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    # Check if no argument is given
    if len(sys.argv) == 1:
        q = ""
    else:
        # otherwise store the argument in q
        q = sys.argv[1]
    # store q in a dictionary
    data = {'q': q}
    # Send the request and get the response
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        # extract the json data from the response
        json_data = response.json()
        # If the json data is not empty, print the id and name
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            # otherwise print No result
            print("No result")
    # If the json data is not valid, print Not a valid JSON
    except ValueError:
        print("Not a valid JSON")

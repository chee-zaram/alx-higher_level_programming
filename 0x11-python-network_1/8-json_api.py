#!/usr/bin/python3
"""
This module sends a `POST` request to the server with the letter as parameter
Server is `http://0.0.0.0:5000/search_user`
The letter must be contained in the variable `q`
If q is not given, set q=""
If response is not properly JSON formatted, print an error message
"""

import requests
from sys import argv


def print_json():
    """Prints a json response"""

    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': argv[1], } if len(argv) > 1 and argv[1] else {'q': "", }

    response = requests.post(url, data=payload)
    try:
        json_obj = response.json()
        if json_obj:
            print(f"[{json_obj.get('id')}] {json_obj.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(f"failed to reach server: {e}")


if __name__ == "__main__":
    print_json()

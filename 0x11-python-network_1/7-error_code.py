#!/usr/bin/python3
"""This module contains code to display body of response if successful"""

import requests
from sys import argv


def handle_errors():
    """Sends a `GET` request to a url and displays the body of the response
    only if the response code is less than 400
    """

    url = argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException:
        print(f"Error code: {response.status_code}")


if __name__ == "__main__":
    handle_errors()

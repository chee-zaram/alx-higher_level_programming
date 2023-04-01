#!/usr/bin/python3
"""Displays the value of header X-Request-Id in response in given URL"""

import requests
from sys import argv


def print_id():
    """Prints value of `X-Request-Id` using `requests` and a given URL"""

    url = argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.headers.get('X-Request-Id'))
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print_id()

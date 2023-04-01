#!/usr/bin/python3
"""Sends a request to given url and displays the body of the response in utf-8
Error handling is allowed here
"""

from urllib.request import Request, urlopen
from urllib.error import URLError
from sys import argv


def print_body_and_handle_errors():
    """Prints the body of the response from a server in utf-8"""
    url = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except URLError as e:
        if hasattr(e, 'code'):
            print(f"Error code: {e.code}")
        elif hasattr(e, 'reason'):
            print(f"Error reason: {e.reason}")
        else:
            print(f"{e}")


if __name__ == "__main__":
    print_body_and_handle_errors()

#!/usr/bin/python3
"""This module contains code which displays value of `X-Request-Id` variable
"""

from urllib.request import Request, urlopen
from urllib.error import URLError
from sys import argv


def print_id():
    """This function prints the `X-Request-Id` value in the response header of
    a url passed in as first argument
    """

    url = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            response_header = response.info()
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print("Reason: ", e.reason)
        elif hasattr(e, 'code'):
            print("The server couldn't fulfill the request.")
            print("Error code: ", e.code)
        exit(1)

    if response_header.get('X-Request-Id'):
        print(response_header['X-Request-Id'])


if __name__ == "__main__":
    print_id()

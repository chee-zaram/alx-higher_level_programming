#!/usr/bin/python3
"""This module contains code to fetch `https://alx-intranet.hbtn.io/status`"""

from urllib.request import urlopen, Request
from urllib.error import URLError


def fetch_body():
    """Fetches the site and displays the body"""

    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)

    try:
        with urlopen(req) as response:
            response_body = response.read()
    except URLError as e:
        if hasattr(e, 'reason'):
            print("Reason: ", e.reason)
        elif hasattr(e, 'code'):
            print("Error code: ", e.code)
    else:
        print("Body response:")
        print("\t- type: {}".format(type(response_body)))
        print("\t- content: {}".format(response_body))
        print("\t- utf8 content: {}".format(response_body.decode("utf-8")))


if __name__ == "__main__":
    fetch_body()

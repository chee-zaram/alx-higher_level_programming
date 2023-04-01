#!/usr/bin/python3
"""This module contains code to `POST` an email to a url passed as argument
unfortunately, they don't permit error handling
"""

from urllib.request import Request, urlopen
from urllib import parse
from sys import argv


def post_email():
    """Sends an email to a server"""

    url = argv[1]
    data = {"email": argv[2], }
    data = parse.urlencode(data)
    data = data.encode("ascii")
    req = Request(url, data)

    with urlopen(req) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    post_email()

#!/usr/bin/python3
"""This module contains code to `POST` an email to a url passed as argument
"""

import requests
from sys import argv


def post_email():
    """Sends an email to a server"""

    url = argv[1]
    email = argv[2]
    payload = {"email": email, }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(response.text)
    else:
        print("[{}] {}".format(response.status_code, response.text))


if __name__ == "__main__":
    post_email()

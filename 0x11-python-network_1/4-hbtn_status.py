#!/usr/bin/python3
"""This module uses `requests` to send a GET request to the URL"""

import requests


def fetch_url():
    """Fetches data from the url `https://alx-intranet.hbtn.io/status`"""
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}\n\t- content: {response.text}")


if __name__ == "__main__":
    fetch_url()

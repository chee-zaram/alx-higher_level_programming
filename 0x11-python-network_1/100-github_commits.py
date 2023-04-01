#!/usr/bin/python3
"""Module to get commit hashes from github user"""

import requests
from sys import argv


def get_commits_from_github():
    """Displays the last 10 commits from a github user"""
    if len(argv) < 3:
        print(f"usage: {argv[0]} <repository> <owner>")
        exit(1)

    repo, owner = argv[1], argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    try:
        commits = requests.get(url, {"Accept": "application/vnd.github+json"})
        commits.raise_for_status()
        commits = commits.json()
        for commit in commits[:10]:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
    except requests.exceptions.HTTPError as e:
        print(f"[{commits.status_code}] {e}")


if __name__ == "__main__":
    get_commits_from_github()

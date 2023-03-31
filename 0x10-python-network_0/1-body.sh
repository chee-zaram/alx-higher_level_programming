#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response
curl -sL -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -sL "$1"

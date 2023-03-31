#!/bin/bash
# takes in a url and sends a request to that url, displaying the size of the body of the response
curl -sI "$1" | grep Content-Length | awk '{print $2}'

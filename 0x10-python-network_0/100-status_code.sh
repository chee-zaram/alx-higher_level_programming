#!/bin/bash
# send a request to url passed as argument and display only status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"

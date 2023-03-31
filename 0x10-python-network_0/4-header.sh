#!/bin/bash
# takes a url as first argument, sends get request to the url with header variable 'X-School-User-Id' with value 98, displays the body of response
curl -sX GET "$1" -H "X-School-User-Id: 98"

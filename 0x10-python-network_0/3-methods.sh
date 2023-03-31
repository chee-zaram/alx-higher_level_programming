#!/bin/bash
# takes in a url as first argument, prints all HTTP methods server will accept
curl -sI "$1" | grep '^Allow:' | sed -e 's/Allow: //'

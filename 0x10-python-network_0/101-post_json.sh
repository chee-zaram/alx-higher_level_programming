#!/bin/bash
# sends a JSON POST request toa url passed as the first argument and file name as second argument, and displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"

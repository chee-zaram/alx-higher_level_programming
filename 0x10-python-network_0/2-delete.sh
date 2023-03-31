#!/bin/bash
# sends a `DELETE` request to the server passed as the first argument and displays the body of the response
curl -s -X DELETE "$1"

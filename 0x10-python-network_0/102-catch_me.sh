#!/bin/bash
# makes request to `0.0.0.0:5000/catch_me` and causes server to respond with `You got me!` in body of response
curl -sLX PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me

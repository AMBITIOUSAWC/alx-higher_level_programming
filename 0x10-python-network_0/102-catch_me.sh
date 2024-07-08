#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me to get a "You got me!" response

curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me

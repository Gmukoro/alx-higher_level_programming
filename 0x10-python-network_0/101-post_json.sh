#!/bin/bash

# Check if the number of arguments is not equal to 2
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 URL JSON_FILE"
    exit 1
fi

# Send POST request with JSON content and display response body
curl -s -H "Content-Type: application/json" -d @"$2" "$1"


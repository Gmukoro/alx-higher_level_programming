#!/bin/bash

# Check if the number of arguments is not equal to 2
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 URL JSON_FILE"
    exit 1
fi

# Extract arguments
url=$1
json_file=$2

# Check if the JSON file exists
if [ ! -f "$json_file" ]; then
    echo "Error: JSON file '$json_file' not found."
    exit 1
fi

# Send POST request with JSON content and display response body
curl -s -X POST -H "Content-Type: application/json" -d @"$json_file" "$url"


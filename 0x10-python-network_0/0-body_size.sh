#!/bin/bash
# script that take in a URL, sends a request 2 dat URL and display the body siz
curl -s "$1" | wc -c

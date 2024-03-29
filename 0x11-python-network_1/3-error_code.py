#!/usr/bin/python3
"""A sscript manages HTTP errors"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv
from urllib.parse import urlencode


def manage_error(url_str: str):
    try:
        req = Request(url_str)
        with urlopen(req) as response:
            body = response.read()
        print(body.decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    try:
        manage_error(argv[1])
    except IndexError:
        raise

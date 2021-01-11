#!/usr/bin/python3
"""displays the value of the X-Request-Id variable
"""
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        req = response.info()
        print(req['X-Request-Id'])

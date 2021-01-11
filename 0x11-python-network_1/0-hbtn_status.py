#!/usr/bin/python3
"""that fetches https://intranet.hbtn.io/status"""
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        typef = type(response.read())
        utf8 = content.decode('utf-8')
        print("Body response:")
        print("    - type: {}".format(typef))
        print("    - content: {}".format(content))
        print("    - utf8 content: {}".format(utf8))

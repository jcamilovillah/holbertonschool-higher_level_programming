#!/usr/bin/python3
"""takes in a letter and sends a POST request
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        d = response.json()
        if d == {}:
            print("No result")
        else:
            print("[{}] {}".format(d.get("id"), d.get("name")))
    except ValueError:
        print("Not a valid JSON")

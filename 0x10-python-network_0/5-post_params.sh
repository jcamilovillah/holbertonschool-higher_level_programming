#!/bin/bash
#sends a POST request to the passed URL, and displays the body of the response
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" 0.0.0.0:5000/route_6

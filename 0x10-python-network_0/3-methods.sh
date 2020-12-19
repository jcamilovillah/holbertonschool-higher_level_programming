#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" | grep -i Allow | awk '{out=""; for(i=2;i<=NF;i++){out=out" "$i}; print out}'

#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
                mayus = ord(i) - 32
        else:
            mayus = ord(i)
        print("{:c}".format(mayus), end="")
    print("")

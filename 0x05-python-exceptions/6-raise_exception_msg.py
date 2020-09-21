#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        print(1/0)
    except ZeroDivisionError:
        print(message)

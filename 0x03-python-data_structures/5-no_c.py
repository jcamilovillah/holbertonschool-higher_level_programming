#!/usr/bin/python3
def no_c(my_string):
    str = ''
    for i in my_string:
        if ord(i) != 67 and ord(i) != 99:
            str += i
    return str

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(0, x):
            if type(my_list[i]) is int:
                print(my_list[i], end="")
        print()
        return x
    except TypeError:
        print()
        return i

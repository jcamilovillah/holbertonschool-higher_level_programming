#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    sum = 0
    for z in range(x):
        try:
            print("{:d}".format(my_list[z]), end="")
            sum += 1
        except (TypeError, ValueError):
            pass
    print()
    return sum

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        sum = 0
        for i in range(0, x):
            if type(my_list[i]) is int:
                print("{}".format(my_list[i]), end="")
                sum += 1
        print()
        return sum
    except (TypeError, ValueError):
        pass

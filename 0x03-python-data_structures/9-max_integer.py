#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list):
        maxi = my_list[0]
        for i in my_list:
            if(i > maxi):
                maxi = i
        return maxi

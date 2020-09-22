#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr as st
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        st.write("Exception: Unknown format code 'd' for object of type 'str'\n")
        return False

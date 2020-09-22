#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    k = 0
    for i in range(0, list_length):
        try:
            k = 0
            k = my_list_1[i]/my_list_2[i]
        except (TypeError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(k)
    return new_list

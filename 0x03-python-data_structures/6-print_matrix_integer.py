#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if(matrix == [[]]):
        print("")    
    for i in range(0, len(matrix)):
        for x in range(0, len(matrix[i])):
            if(x + 1 == len(matrix[i])):
                print("{}".format(matrix[i][x]), end='')
            else:
                print("{}".format(matrix[i][x]), end=' ')
        print("")

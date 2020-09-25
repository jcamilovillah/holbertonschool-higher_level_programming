#!/usr/bin/python3
"""Function that return a new matrix"""


def matrix_divided(matrix, div):
    """divide a matrix
    args:
        matrix: original
        div: number for div
    """
    if matrix:
        new_matrix = []
        var = 0
        for x in matrix:
            new_matrix.append([])
            for z in x:
                if div == 0:
                    raise ZeroDivisionError("division by zero")
                if len(x) != len(matrix[0]):
                    raise TypeError("Each row of the matrix\
 must have the same size")
                elif type(z) != int and type(z) != float:
                    raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
                elif type(div) != int and type(div) != float:
                    raise TypeError("div must be a number")
                else:
                    new_matrix[var].append(round((z / div), 2))
            var += 1
        return new_matrix
    raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")

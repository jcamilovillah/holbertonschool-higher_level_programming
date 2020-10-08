#!/usr/bin/python3
def pascal_triangle(n):
    """Pascal"""
    if n <= 0:
        empty = []
        return empty
    lista = [[1], [1, 1]]
    for i in range(1, n):
        linea = [1]
        for j in range(0, len(lista[i]) - 1):
            linea.extend([lista[i][j] + lista[i][j+1]])
        linea += [1]
        lista.append(linea)
    return lista

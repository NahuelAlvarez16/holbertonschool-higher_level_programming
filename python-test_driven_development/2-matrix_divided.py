#!/usr/bin/python3
""" 2-matrix_divided module """


def matrix_divided(matrix, div):
    """ function to divide a matrix with a number """
    if type(div) is float:
        div = int(div)
    if type(div) != int and type(div) != float:
                raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    matrix_len = len(matrix[0])
    new_matrix = []
    for i in range(len(matrix)):
        if len(matrix[i]) != matrix_len:
                raise TypeError("Each row of the matrix must have the same size")
        matrix_len = len(matrix[i])
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_matrix.append([])
        for x in range(len(matrix[i])):
            if type(matrix[i][x]) != int and type(matrix[i][x]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[i].append(matrix[i][x] / float(div))
    
#!/usr/bin/python3
""" 2-matrix_divided module """


def matrix_divided(matrix, div):
    """ function to divide a matrix with a number """
    if type(div) != int and type(div) != float:
                raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    matrix_len = len(matrix[0])
    new_matrix = []
    for i, row in enumerate(matrix):
        if len(row) != matrix_len:
                raise TypeError(
                    "Each row of the matrix must have the same size")
        matrix_len = len(row)
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        new_matrix.append([])
        for x in range(len(row)):
            if type(row[x]) != int and type(row[x]) != float:
                raise TypeError(
                    "matrix must be a matrix \
(list of lists) of integers/floats")
            new_matrix[i].append(round(row[x] / float(div), 2))
    return new_matrix

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        rows = len(matrix)
        columns = len(matrix[0])

        for r in range(0, rows):
            for c in range(0, columns):
                print("{:d}".format(matrix[r][c]), end="")
                if c != columns - 1:
                    print(end=" ")
            print()

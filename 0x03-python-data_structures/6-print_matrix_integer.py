#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            end = ""
            if i < len(row):
                end = " "
            print("{}".format(row[i]), end=end)
        print()

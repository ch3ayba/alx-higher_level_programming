#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for d in matrix:
        print(' '.join('{:d}'.format(e)for e in d))

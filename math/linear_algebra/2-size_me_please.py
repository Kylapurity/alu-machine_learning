#!/usr/bin/env python3
def matrix_shape(matrix):
    findshape = []
    while isinstance(matrix, list):
        findshape.append(len(matrix))
        matrix = matrix[0]
    return findshape

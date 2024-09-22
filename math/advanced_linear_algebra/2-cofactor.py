#!/usr/bin/env python3
'''
This module contains the function to calculate the cofacor of a matrix.
'''


def cofactor(matrix):
    '''
    Returns the cofactor matrix of a matrix.
    '''
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty list")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not all(len(matrix) == len(row) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1:
        return [[1]]
    if len(matrix) == 2:
        return [[matrix[1][1], -matrix[1][0]], [-matrix[0][1], matrix[0][0]]]
    cofactor_matrix = []
    for i in range(len(matrix)):
        cofactor_row = []
        for j in range(len(matrix[i])):
            minor = []
            for k in range(len(matrix)):
                if k == i:
                    continue
                row = []
                for l in range(len(matrix[i])):
                    if l == j:
                        continue
                    row.append(matrix[k][l])
                minor.append(row)
            cofactor_row.append(determinant(minor) * (-1) ** (i + j))
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix


def determinant(matrix):
    '''
    Returns the determinant of a matrix.
    '''
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty list")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not all(len(matrix) == len(row) for row in matrix):
        raise ValueError("matrix must be a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for i, num in enumerate(matrix[0]):
        minor = []
        for row in matrix[1:]:
            minor_row = []
            for j, n in enumerate(row):
                if j != i:
                    minor_row.append(n)
            minor.append(minor_row)
        det += num * (-1) ** i * determinant(minor)
    return det

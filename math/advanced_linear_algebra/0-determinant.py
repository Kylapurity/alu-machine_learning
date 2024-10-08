#!/usr/bin/env python3
"""Defne a fuction that caculate the determinat of a matrix"""


def determinant(matrix):
    """ Calculate the determinant of a square matrix. """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
       for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
# Recursive case: nxn matriv
    det = 0
    for i in range(n):
        sign = (-1) ** i
        sub_det = determinant([row[:i] + row[i + 1:] for row in matrix[1:]])
        det += sign * matrix[0][i] * sub_det
    return det

#!/usr/bin/env python3
'''
This module contains the function to calculate the adjugate of a matrix.
'''


def adjugate(matrix):
    '''
    Returns the adjugate of a matrix.
    '''
    if not matrix:
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not matrix:
        raise ValueError("matrix must be a non-empty square matrix")
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return [[1]]

    adjugate_matrix = []
    for i in range(len(matrix)):
        adjugate_matrix.append([])
        for j in range(len(matrix)):
            sub_matrix = [row[:j] + row[j + 1:]
     for row in (matrix[:i] + matrix[i + 1:])]
            sign = (-1) ** (i + j)
            adjugate_matrix[i].append(sign * determinant(sub_matrix))

    return list(map(list, zip(*adjugate_matrix)))


def determinant(matrix):
    '''
    Returns the determinant of a matrix.
    '''
    if not matrix:
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not matrix:
        raise ValueError("matrix must be a square matrix")
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * determinant([row[:c] + row[c + 1:] 
     for row in matrix[1:]])
    return det

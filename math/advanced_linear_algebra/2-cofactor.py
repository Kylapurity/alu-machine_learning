#!/usr/bin/env python3
'''
This module contains the function to calculate the cofacor of a matrix.
'''


def cofactor(matrix):
    '''
    Function to calculate the cofactor of a matrix.
    '''
    if not isinstance(matrix, list) or len(matrix) == 0\
       or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    cofactor_matrix = []
    for i in range(len(matrix)):
        cofactor_matrix.append([])
        for j in range(len(matrix)):
            minor_matrix = minor(matrix, i, j)
            cofactor_matrix[i].append(((-1) ** (i + j)) *
                 determinant(minor_matrix))
    return cofactor_matrix


def minor(matrix, i, j):
    '''
    Function to calculate the minor of a matrix.
    '''
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]


def determinant(matrix):
    '''
    Function to calculate the determinant of a matrix.
    '''
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(len(matrix)):
        submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(submatrix)
    return det

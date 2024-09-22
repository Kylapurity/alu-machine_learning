#!/usr/bin/env python3
'''
This module contains the function to calculate the cofacor of a matrix.
'''



def cofactor(matrix):
    '''
    Function to calculate the cofactor of a matrix.
    '''
    n = len(matrix)
    cofactor_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # Calculate the minor matrix
            minor_matrix = minor(matrix, i, j)
            # Calculate the determinant of the minor matrix
            minor_det = determinant(minor_matrix)
            # Calculate the cofactor
            cofactor_matrix[i][j] = ((-1) ** (i + j)) * minor_det
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

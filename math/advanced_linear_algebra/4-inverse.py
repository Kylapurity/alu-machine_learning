#!/usr/bin/env python3
'''
This module contains the function to calculate the Inverse of a matrix.
'''


def inverse(matrix):
    '''
    This function calculates the inverse of a matrix.
    '''
    # Check if the matrix is square
    if not isinstance(matrix, list) or len(matrix) == 0 or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if not all(isinstance(element, (int, float)) 
for row in matrix for element in row):
        raise TypeError("matrix should contain only integers and floats")
    # Check if the matrix is invertible
    if len(matrix) == 1:
        if matrix[0][0] == 0:
            return None
        else:
            return [[1 / matrix[0][0]]]
    if len(matrix) == 2:
        if matrix[0][0] * matrix[1][1] == matrix[0][1] * matrix[1][0]:
            return None
    # Calculate the determinant of the matrix
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    # Check if the determinant is zero
    if determinant == 0:
        return None
    # Calculate the adjugate of the matrix
    adjugate = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
    # Calculate the inverse of the matrix
    inverse = [[adjugate[0][0] / determinant, adjugate[0][1] / determinant],
               [adjugate[1][0] / determinant, adjugate[1][1] / determinant]]
    return inverse

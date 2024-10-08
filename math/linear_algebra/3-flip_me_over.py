#!/usr/bin/env python3
"""Defines function that transposes a 2D matrix"""


def matrix_transpose(matrix):
    '''Returns the transpose of a 2D matrix'''
    return [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]

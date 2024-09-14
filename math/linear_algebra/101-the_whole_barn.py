#!/usr/bin/env python3
"""Define a function that will add the 2 matrices and result to either a interger and float"""


def add_matrices(mat1, mat2):
    """Add two matrices"""
    if len(mat1) != len(mat2):
        return None
    if isinstance(mat1[0], list):
        return [add_matrices(mat1[i], mat2[i]) for i in range(len(mat1))]
    return [mat1[i] + mat2[i] for i in range(len(mat1))]

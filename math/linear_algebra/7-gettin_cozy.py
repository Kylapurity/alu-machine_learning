#!/usr/bin/env python3
"""Define a cat_matrices2D function"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenate two 2D matrices along a specific axis"""
    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    if axis == 1 and len(mat1) != len(mat2):
        return None
    return [row.copy() for row in mat1] + [row.copy() for row in mat2]

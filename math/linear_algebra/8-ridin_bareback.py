#!/usr/bin/env python3
"""Define Mul of the same dimension"""


def mat_mul(mat1, mat2):
    """Matrix multiplication"""
    if len(mat1[0]) != len(mat2):
        return None
    return [[sum(a * b for a, b in zip(row, col))
             for col in zip(*mat2)] for row in mat1]

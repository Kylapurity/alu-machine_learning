#!/usr/bin/env python3
"""Define Np shape"""


import numpy as np
def np_shape(matrix):
    """Function that calculates the shape of a numpy.ndarray"""
    return matrix.shape

mat1 = np.array([1, 2, 3, 4, 5, 6])
mat2 = np.array([])
mat3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                 [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])
print(np_shape(mat1))
print(np_shape(mat2))
print(np_shape(mat3))

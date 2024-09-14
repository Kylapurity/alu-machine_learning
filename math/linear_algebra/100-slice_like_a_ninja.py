#!/usr/bin/env python3

import numpy as np

def np_slice(matrix, axes={}):
    slices = [slice(None)] * matrix.ndim
    for axis, slice_ in axes.items():
        slices[axis] = slice(*slice_)
    return matrix[tuple(slices)]

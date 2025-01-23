#!/usr/bin/env python3
'''
This module contains
'''
import numpy as np


def definiteness(matrix):
    '''
    This function determines the definiteness of a matrix.
    '''
    # Check if matrix is a numpy.ndarray
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None
    # Check if matrix is symmetric
    if not np.allclose(matrix, matrix.T):
        return None
    try:
        # Compute eigenvalues
        eigenvalues = np.linalg.eigvals(matrix)
    except np.linalg.LinAlgError:
        # Matrix is not valid (e.g., contains NaN or inf)
        return None
    # Check if matrix is positive definite
    if np.all(np.linalg.eigvals(matrix) > 0):
        return "Positive definite"
    # Check if matrix is positive semi-definite
    if np.all(np.linalg.eigvals(matrix) >= 0):
        return "Positive semi-definite"
    # Check if matrix is negative definite
    if np.all(np.linalg.eigvals(matrix) < 0):
        return "Negative definite"
    # Check if matrix is negative semi-definite
    if np.all(np.linalg.eigvals(matrix) <= 0):
        return "Negative semi-definite"
    # Check if matrix is indefinite
    return "Indefinite"
# Check if matrix is singular
    if np.all(np.linalg.eigvals(matrix) == 0):
        return "Singular"

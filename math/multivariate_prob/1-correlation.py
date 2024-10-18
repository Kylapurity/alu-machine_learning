#!/usr/bin/env 
'''Define  a function that calculates a correlation matrix'''
import numpy as np


def correlation(C):
    '''Calculate the correlation matrix of a numpy array'''
    if not isinstance(C, np.ndarray):
        raise TypeError('C must be a numpy.ndarray')
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError('C must be a 2D square matrix')
    diag = np.diag(np.sqrt(np.diag(C)))
    inv_diag = np.linalg.inv(diag)
    correlation = np.dot(np.dot(inv_diag, C), inv_diag)
    return correlation

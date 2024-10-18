#!/usr/bin/env python3
'''Define a function that calculates the calculates the intersection of obtaining this data'''


import numpy as np


def intersection(x, n, P, Pr):
    '''Calculate the intersection of obtaining this data with the various hypothetical probabilities'''
    if type(n) is not int or n <= 0:
        raise ValueError('n must be a positive integer')
    if type(x) is not int or x < 0:
         text = "x must be an integer that is greater than or equal to 0"
        raise ValueError(text)
    if x > n:
        raise ValueError('x cannot be greater than n')
    if type(P) is not np.ndarray or len(P.shape) != 1:
        raise TypeError('P must be a 1D numpy.ndarray')
    if not all(i >= 0 and i <= 1 for i in P):
        raise ValueError('All values in P must be in the range [0, 1]')
    if type(Pr) is not np.ndarray or P.shape != Pr.shape:
        raise TypeError('Pr must be a numpy.ndarray with the same shape as P')
    if not all(i >= 0 and i <= 1 for i in Pr):
        raise ValueError('All values in Pr must be in the range [0, 1]')
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError('Pr must sum to 1')
    fact = np.math.factorial
    comb = fact(n) / (fact(x) * fact(n - x))
    likelihood = comb * (P ** x) * ((1 - P) ** (n - x))
    return likelihood * Pr

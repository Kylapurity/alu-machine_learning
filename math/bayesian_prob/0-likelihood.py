#!/usr/bin/env python3
'''Define a function that calculates the likelihood of obtaining this data'''

import numpy as np


def likelihood(x, n, P):
    '''Function that calculates the likelihood of obtaining this data given'''

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    # Calculate the factorial combination term (n choose x)
    fact_n = np.math.factorial(n)
    fact_x = np.math.factorial(x)
    fact_nx = fact_n / (fact_x * np.math.factorial(n - x))

    # Compute the likelihood for each probability in P
    likelihood_values = fact_nx * (P ** x) * ((1 - P) ** (n - x))

    return likelihood_values

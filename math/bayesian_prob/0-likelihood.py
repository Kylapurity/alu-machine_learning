#!/usr/bin/env python3
'''Define a function that calculates the likelihood of obtaining 
this data given various hypothetical probabilities of developing severe side effects'''


def likelihood(x, n, P):
    '''Function that calculates the likelihood of obtaining 
    this data given various hypothetical probabilities of developing severe side effects'''
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if type(P) is not float or P < 0 or P > 1:
        raise ValueError("P must be a float in the range [0, 1]")
    fact_n = 1
    fact_x = 1
    fact_diff = 1
    for i in range(1, n + 1):
        fact_n *= i
    for i in range(1, x + 1):
        fact_x *= i
    for i in range(1, n - x + 1):
        fact_diff *= i
    likelihood = (fact_n / (fact_x * fact_diff)) * (P ** x) * ((1 - P) ** (n - x))
    return likelihood

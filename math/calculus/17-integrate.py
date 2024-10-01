#!/usr/bin/env python3
"""Define the function that calculates the   poly_integral(poly, C=0) """


def poly_integral(poly, C=0):
    """Calculate the integral of a polynomial"""
    if not isinstance(poly, list) or not all(isinstance(i, (int, float))
                                             for i in poly) or not isinstance(C, (int, float)):
        return None
    if len(poly) == 0:
        return None
    integral = [C]
    for i in range(len(poly)):
        if poly[i] == 0:
            continue
        integral.append(poly[i] / (i + 1))
    return integral

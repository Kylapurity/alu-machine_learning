#!/usr/bin/env python3
'''Define a function that calculates MultiNormal that represents a Multivariate Normal distribution'''

import numpy as np

class MultiNormal:
    '''A class that represents a Multivariate Normal distribution'''

    def __init__(self, data):
        '''Initialize the MultiNormal instance with data'''
        self.data = data
        self.mean = np.mean(data, axis=0).reshape(-1, 1)
        self.cov = self.calculate_covariance(data)
        self.inv_cov = np.linalg.inv(self.cov)
        self.det_cov = np.linalg.det(self.cov)
        self.dim = data.shape[1]
        self.norm_const = 1 / (np.sqrt((2 * np.pi) ** self.dim * self.det_cov))

    def calculate_covariance(self, data):
        '''Calculate the covariance matrix manually'''
        mean = np.mean(data, axis=0)
        data_centered = data - mean
        cov_matrix = np.dot(data_centered.T, data_centered) / (data.shape[0] - 1)
        return cov_matrix

    def pdf(self, x):
        '''Calculate the probability density function for a given x'''
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        if x.shape != (self.dim, 1):
            raise ValueError(f"x must have the shape ({self.dim}, 1)")

        diff = x - self.mean
        exponent = -0.5 * np.dot(diff.T, np.dot(self.inv_cov, diff))
        return float(self.norm_const * np.exp(exponent))

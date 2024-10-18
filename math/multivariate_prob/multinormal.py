#!/usr/bin/env python3
'''A module that defines a MultiNormal class to represent a Multivariate Normal distribution'''

import numpy as np


class MultiNormal:
    '''A class that represents a Multivariate Normal distribution'''

    def __init__(self, data):
        '''
        Initialize the MultiNormal instance with data
        Args:
            data (numpy.ndarray): data set of shape (d, n)
        '''
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)
        self.cov = self.calculate_covariance(data)
        self.inv_cov = np.linalg.inv(self.cov)
        self.det_cov = np.linalg.det(self.cov)
        self.dim = data.shape[0]  # d is the number of dimensions
        self.norm_const = 1 / (np.sqrt((2 * np.pi) ** self.dim * self.det_cov))

    def calculate_covariance(self, data):
        '''Calculates the covariance matrix manually without using numpy.cov'''
        mean = np.mean(data, axis=1, keepdims=True)
        data_centered = data - mean
        cov_matrix = np.dot(data_centered, data_centered.T) / (data.shape[1] - 1)
        return cov_matrix

    def pdf(self, x):
        '''
        Calculate the probability density function (PDF) for a given point
        Args:
            x (numpy.ndarray): data point of shape (d, 1)
        Returns:
            float: the value of the PDF at the given point
        '''
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        if x.shape != (self.dim, 1):
            raise ValueError(f"x must have the shape ({self.dim}, 1)")

        diff = x - self.mean
        exponent = -0.5 * np.dot(diff.T, np.dot(self.inv_cov, diff))
        return float(self.norm_const * np.exp(exponent))

#!/usr/bin/env python3
"""
Module that performs pooling on images.
"""

import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    Performs pooling on images.
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    # Calculate the dimensions of the output
    output_h = (h - kh) // sh + 1
    output_w = (w - kw) // sw + 1

    # Initialize the output array
    output = np.zeros((m, output_h, output_w, c))

    # Perform the pooling
    for i in range(output_h):
        for j in range(output_w):
            # Extract the region of interest
            region = images[:, i*sh:i*sh+kh, j*sw:j*sw+kw, :]
            if mode == 'max':
                # Perform max pooling
                output[:, i, j, :] = np.max(region, axis=(1, 2))
            elif mode == 'avg':
                # Perform average pooling
                output[:, i, j, :] = np.mean(region, axis=(1, 2))

    return output

#!/usr/bin/env python3
"""
Module that performs a same convolution on grayscale images.
"""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Performs a same convolution on grayscale images.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    # Calculate the padding for height and width
    pad_h = kh // 2
    pad_w = kw // 2

    # Pad the images with zeros
    padded_images = np.pad(images, ((0, 0), (pad_h, pad_h), (pad_w, pad_w)),
                           mode='constant')

    # Initialize the output array
    output = np.zeros((m, h, w))

    # Perform the convolution
    for i in range(h):
        for j in range(w):
            # Extract the region of interest
            region = padded_images[:, i:i+kh, j:j+kw]
            # Perform element-wise multiplication and sum the result
            output[:, i, j] = np.sum(region * kernel, axis=(1, 2))

    return output

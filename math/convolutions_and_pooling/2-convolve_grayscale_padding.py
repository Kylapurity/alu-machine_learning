#!/usr/bin/env python3
"""
Module that performs a convolution on grayscale images with custom padding.
"""

import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    Performs a convolution on grayscale images with custom padding.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    # Pad the images with zeros
    padded_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), mode='constant')

    # Calculate the dimensions of the output
    output_h = h + 2 * ph - kh + 1
    output_w = w + 2 * pw - kw + 1

    # Initialize the output array
    output = np.zeros((m, output_h, output_w))

    # Perform the convolution
    for i in range(output_h):
        for j in range(output_w):
            # Extract the region of interest
            region = padded_images[:, i:i+kh, j:j+kw]
            # Perform element-wise multiplication and sum the result
            output[:, i, j] = np.sum(region * kernel, axis=(1, 2))

    return output

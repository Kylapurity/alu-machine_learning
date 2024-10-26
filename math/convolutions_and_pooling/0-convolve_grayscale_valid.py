#!/usr/bin/env python3
import numpy as np

def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images.

    Args:
        images (numpy.ndarray): Shape (m, h, w) containing multiple grayscale images.
        kernel (numpy.ndarray): Shape (kh, kw) containing the kernel for the convolution.

    Returns:
        numpy.ndarray: Containing the convolved images.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    # Calculate the dimensions of the output
    output_h = h - kh + 1
    output_w = w - kw + 1

    # Initialize the output array
    output = np.zeros((m, output_h, output_w))

    # Perform the convolution
    for i in range(output_h):
        for j in range(output_w):
            # Extract the region of interest
            region = images[:, i:i+kh, j:j+kw]
            # Perform element-wise multiplication and sum the result
            output[:, i, j] = np.sum(region * kernel, axis=(1, 2))

    return output

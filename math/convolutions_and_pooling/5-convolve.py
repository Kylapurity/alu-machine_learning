#!/usr/bin/env python3
"""
Module that performs a convolution on images using multiple kernels.
"""

import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """
    Performs a convolution on images using multiple kernels.
    """
    m, h, w, c = images.shape
    kh, kw, kc, nc = kernels.shape
    sh, sw = stride

    if kc != c:
        raise ValueError(
            "The number of channels in the kernels must match the number "
            "of channels in the images"
        )

    if padding == 'same':
        ph = ((h - 1) * sh + kh - h) // 2 + 1
        pw = ((w - 1) * sw + kw - w) // 2 + 1
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    # Pad the images with zeros
    padded_images = np.pad(
        images, ((0, 0), (ph, ph), (pw, pw), (0, 0)), mode='constant'
    )

    # Calculate the dimensions of the output
    output_h = (h + 2 * ph - kh) // sh + 1
    output_w = (w + 2 * pw - kw) // sw + 1

    # Initialize the output array
    output = np.zeros((m, output_h, output_w, nc))

    # Perform the convolution
    for k in range(nc):
        for i in range(output_h):
            for j in range(output_w):
                # Extract the region of interest
                region = padded_images[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :]
                # Perform element-wise multiplication and sum the result
                output[:, i, j, k] = np.sum(
                    region * kernels[:, :, :, k],
                    axis=(1, 2, 3)
                )

    return output

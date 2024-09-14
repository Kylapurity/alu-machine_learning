#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Define arrays"""


def add_arrays(arr1, arr2):
    """Add two arrays"""
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]

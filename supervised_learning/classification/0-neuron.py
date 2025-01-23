#!/usr/bin/env python3
'''
The script class Neuron that defines a single neuron performing binary classification

'''
import numpy as np

class Neuron:

    def __init__(self, nx):
        '''
        Initializes the neuron with the number of input features
        '''
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
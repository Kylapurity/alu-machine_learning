#!/usr/bin/env python3
'''Define a  Create a class Normal that represents a normal distribution
'''

class Normal:
    '''Normal distribution class
    '''
def __init__(self, data=None, mean=0., stddev=1.):
    '''Constructor
    '''
    if data is None:
        if stddev <= 0:
            raise ValueError('stddev must be a positive value')
        self.stddev = float(stddev)
        self.mean = float(mean)
    else:
        if not isinstance(data, list):
            raise TypeError('data must be a list')
        if len(data) < 2:
            raise ValueError('data must contain multiple values')
        self.mean = sum(data) / len(data)
        self.stddev = (sum([(x - self.mean) ** 2 for x in data]) / len(data)) ** 0.5

def probability(self, x):
    '''Calculates the z-score of a given x-value
    '''
    return (1 / (self.stddev * (2 * 3.1415926536) ** 0.5)) * \
        2.7182818285 ** ((x - self.mean) ** 2 / (-2 * self.stddev ** 2))

def z_score(self, x):
    '''Calculates the z-score of a given x-value
    '''
    return (x - self.mean) / self.stddev

def x_value(self, z):
    '''Calculates the x-value of a given z-score
    '''
    return z * self.stddev + self.mean

def pdf(self, x):
    '''Calculates the value of the PDF for a given x-value
    '''
    return (1 / (self.stddev * (2 * 3.1415926536) ** 0.5)) * \
        2.7182818285 ** ((x - self.mean) ** 2 / (-2 * self.stddev ** 2))

def cdf(self, x):
    '''Calculates the value of the CDF for a given x-value
    '''
    x = (x - self.mean) / (self.stddev * 2 ** 0.5)
    return (1 + (x - x ** 3 / 3 + x ** 5 / 10 - x ** 7 / 42 + x ** 9 / 216) * 2 / 3.1415926536 ** 0.5) / 2

def inv_cdf(self, x):
    '''Calculates the value of the CDF for a given x-value
    '''
    return self.mean + x * self.stddev * 2 ** 0.5

def __str__(self):
    '''Return the string representation of the normal distribution
    '''
    return 'Normal({}, {})'.format(self.mean, self.stddev)

def __repr__(self):
    '''Return the string representation of the normal distribution
    '''
    return 'Normal({}, {})'.format(self.mean, self.stddev)

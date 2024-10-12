#!/usr/bin/env python3
'''Define a Create a class Exponential that represents an exponential distribution:'''

class Exponential:
    '''Exponential distribution'''

    def __init__(self, data=None, lambtha=1.):
        '''Constructor'''
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = len(data) / sum(data)
            self.data = data

    def probability(self, x):
        '''Calculates the value of the PDF for a given time period'''
        if x < 0:
            return 0
        return self.lambtha * (2.7182818285 ** (-self.lambtha * x))

    def cdf(self, x):
        '''Calculates the value of the CDF for a given time period'''
        if x < 0:
            return 0
        return 1 - (2.7182818285 ** (-self.lambtha * x))

    def mean(self):
        '''Calculates the mean of the distribution'''
        return 1 / self.lambtha

    def std(self):
        '''Calculates the standard deviation of the distribution'''
        return (1 / self.lambtha) ** 0.5

    def __str__(self):
        '''Returns a string representation of the distribution'''
        return 'Exponential distribution for data with lambtha: {}'.format(self.lambtha)

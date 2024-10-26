#!/usr/bin/env python3
'''Define Create a class Binomial that represents a binomial distribution'''


class Binomial:
    '''Binomial distribution class'''
    def __init__(self, data=None, n=1, p=0.5):
        '''Constructor'''
        if data is None:
            if n <= 0:
                raise ValueError('n must be a positive value')
            if p <= 0 or p >= 1:
                raise ValueError('p must be greater than 0 and less than 1')
            self.n = n
            self.p = p
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            mean = sum(data) / len(data)
            variance = sum([(x - mean) ** 2 for x in data]) / len(data)
            p = 1 - variance / mean
            n = round(mean / p)
            p = mean / n
            self.n = n
            self.p = p

    def factorial(self, k):
        '''Helper method to calculate factorial'''
        if k == 0 or k == 1:
            return 1
        result = 1
        for i in range(2, k + 1):
            result *= i
        return result

    def pmf(self, k):
        '''Calculates the value of the PMF for a given number of successes'''
        if type(k) is not int:
            k = int(k)
        if k < 0 or k > self.n:
            return 0
        n = self.n
        p = self.p
        # Calculate binomial coefficient: n! / (k! * (n-k)!)
        binom_coeff = self.factorial(n) / (
            self.factorial(k) * self.factorial(n - k)
        )
        pmf = binom_coeff * (p ** k) * ((1 - p) ** (n - k))
        return pmf

    def cdf(self, k):
        '''Calculates the value of the CDF for a given number of successes'''
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf

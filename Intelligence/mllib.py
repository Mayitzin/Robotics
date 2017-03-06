# -*- coding: utf-8 -*-
"""Personalized library of Machine Learning

@author: Mario Garcia
"""

import numpy as np


def ber(X, p=0.5):
    """Bernoulli Distribution
    Computes the probability distribution of an independient random variable,
    which takes the value 1 with success probability of p; and the value 0 with
    failure probability of q=1-p.

    Default is p = 0.5 to give a fair and equal distribution for each outcome.

    The probabilty mass function f over possible outcomes k, is:
                ,-
                |  p        if k = 1
    f(k | p) = <
                |  1 - p    if k = 0
                `-

    also defined as:

    f(k | p) = p^k * (1 - p)^(1-k)        for k in {0,1}

    see:
    - https://en.wikipedia.org/wiki/Bernoulli_distribution
    - http://mathworld.wolfram.com/BernoulliDistribution.html
    """
    f = p**X * (1.0-p)**(1-X)
    # Get Properties of the distribution
    mean = p
    var = p*(1.0-p)
    std = np.sqrt(var)
    # Return the values
    return f, mean, var, std


def pdf(X, m=0.0, s=1.0):
    """Probability Density Function (Gaussian Distribution)
    This function builds the probability density of the normal distribution:

    pdf(X | m, s^2) = exp(-(x-m)^2/2*s^2) / sqrt(2*s^2*Pi)

    where:
        m is the mean or expectation of the distribution.
            Default: m = 0.0
        s is the standard deviation.
            Default: s = 1.0
        s^2 is the variance.
            Default: s^2 = 1.0

    see:
    - https://en.wikipedia.org/wiki/Normal_distribution
    """
    f = np.zeros(np.shape(X))
    normalizer = 1.0/np.sqrt(2.0*s*s*np.pi)
    for i in range(len(X)):
        f[i] = normalizer * np.exp(-(X[i]-m)**2/(2.0*s*s))
    return f


def sigmoid(x):
    return 1./(1+np.exp(-x))


def binomialCoefficient(n, k):
    if 0<=k<n:
        b = 1
        for i in range(k):
            b = b * (n-i)/(i+1)
        return b
    else:
        return 0


def softmax(z):
    return np.exp(z)/np.sum(np.exp(z))


def test_ber(n=5,p=0.5):
    """Testing function for the Bernoulli distribution
    Default:
        n = 5      # Number of samples
        p = 0.5    # Probability of success
    """
    print "\nTest of Bernoulli Distribution"
    print "------------------------------"
    X = np.random.random_integers(0,1,size=(n))
    print "X = %d random sampled outcomes (Bernoulli trials) =\n"%(n), X
    f, mean, var, std = ber(X,p)
    print "\nP(X ; %.2f) =\n"%(p), f, "\n"
    print "  mean = %.2f" % mean
    print "  var = %.3f" % var
    print "  std = %.4f" % std




###### Testing the Functions ######

p = 0.3
test_ber(5,p)

n = 4
k = 2
print binomialCoefficient(n, k)

# X = np.linspace(-4.0, 4.0, num=40)
# Y = pdf(X)
# import matplotlib.pyplot as plt
# l1 = plt.plot(X, Y, 'r-')
# plt.show()

# from scipy.stats import multivariate_normal
# x, y = np.mgrid[-1:1:0.01, -1:1:0.01]
# pos = np.empty(x.shape + (2,))
# pos[:,:,0] = x
# pos[:,:,1] = y
# mean = [0.5, -0.2]
# cov = [[2.0, 0.3],[0.3, 0.5]]
# rv = multivariate_normal(mean, cov)
# plt.contourf(x,y,rv.pdf(pos))
# plt.show()

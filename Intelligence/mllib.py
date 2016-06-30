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
                /
                | p        if k = 1
    f(k ; p) = <
                | 1 - p    if k = 0
                \

    also defined as:

    f(k ; p) = p^k * (1-p)^(1-k)        for k in {0,1}

    This function computes it with both methods

    see:
    - https://en.wikipedia.org/wiki/Bernoulli_distribution
    - http://mathworld.wolfram.com/BernoulliDistribution.html
    """
    f1 = np.zeros(np.shape(X))
    f2 = np.zeros(np.shape(X))
    for k in range(len(X)):
        if X[k]==0:   f1[k] = 1.0-p
        elif X[k]==1: f1[k] = p
        f2[k] = p**X[k] * (1.0-p)**(1-X[k])
    # Get Properties of the distribution
    mean = p
    var = p*(1.0-p)
    std = np.sqrt(var)
    # Return the values
    return f1, f2, mean, var, std


def test_ber(n=5,p=0.5):
    print "\nTest of Bernoulli Distribution"
    print "------------------------------"
    X = np.random.random_integers(0,1,size=(n))
    print "X = %d random sampled outcomes (Bernoulli trials) =\n"%(n), X
    f1,_, mean, var, std = ber(X,p)
    print "\nP(X ; %.2f) =\n"%(p), f1, "\n"
    print "  mean = %.2f"%mean
    print "  var = %.3f"%var
    print "  std = %.4f"%std


test_ber(6,0.3)
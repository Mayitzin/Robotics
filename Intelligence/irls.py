"""Iteratively reweighted least squares (IRLS)

Implementation in Python of the IRLS algorithm as presented by Nando de Freitas
in his lectures on Machine Learning on 16.03.2014.
"""

from __future__ import division
import numpy as np

def logistic(a):
    return 1.0 / (1 + np.exp(-a))


def irls(X,y):
    theta = np.zeros(X.shape[1])
    theta_ = np.inf
    while max(abs(theta-theta_))>1e-6:
        a = np.dot(X,theta)
        pi = logistic(a)
        SX = X * (pi-pi*pi).reshape(-1,1)
        XSX = np.dot(X.T, SX)
        SXTheta = np.dot(SX, theta)
        theta_ = theta
        theta = np.linalg.solve(XSX, np.dot(X.T, SXTheta + y -pi))
    return theta


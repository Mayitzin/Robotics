# -*- coding: utf-8 -*-
"""
This script plots the results of a Kalman Filter with different parameter
values.

History:
    12.02.2016. First Implementation.

@author: Mario Garcia
www.mayitzin.com
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as lin


def kf(xhat, z, A, P, Q, R, H):
    """
    The linear Kalman Filter computes the current state m-by-1 vector
    xhat and its m-by-m Covariance matrix P, given the parameters of the
    previous state.
        m is the number of elements in array xhat.
        n is the length of array z (number of sensor signals to compare).
    """
    m = len(xhat)
    n = len(z)
    I = np.eye(m)
    # KF - Prediction
    xhat = np.dot(A, xhat)
    P    = np.dot(A, np.dot(P, A.T)) + Q
    # KF - Update
    S    = np.dot(H, np.dot(P, H.T)) + R
    K    = np.dot(P, np.dot(H.T, lin.inv(S)))
    v    = z.reshape((n,1)) - np.dot(H, xhat)
    xhat = xhat + np.dot(K, v)
    P    = np.dot((I - np.dot(K, H)), P)
    return xhat, P


def function(x):
    y = []
    [y.append( 2.0*np.sin(5.0*x[i])*np.cos(0.5*x[i]) ) for i in range(len(x))]
    return y


n = 500
x = np.arange(0.,5.,5./n)
y = np.array(function(x))

# Added random noise
mu, sigma = 0, 0.2
s = np.random.normal(mu, sigma, n)
r = y + s

plt.plot(x,y)
plt.plot(x,r,'r.')
plt.show()
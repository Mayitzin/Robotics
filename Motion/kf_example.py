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


def function(x, w=[2.0, 5.0, 0.5]):
    y = []
    [y.append( w[0]*np.sin(w[1]*x[i])*np.cos(w[2]*x[i]) ) for i in range(len(x))]
    return y

# Generate the points
n = 250
x = np.arange(0.,5.,5./n)
y = np.array(function(x))

# Add random noise
mu, sigma = 0, 0.05
s = np.random.normal(mu, sigma, n)
r = y + s

# Static elements of KF
z = r.reshape((1,n))
A = np.array([[1.0]])
P = np.array([[1.0]])
H = np.array([[1.0]])

# Variable elements of KF
sigmas = sigma*np.array([0.1, 0.5, 1.0])
m = len(sigmas)
xhat = np.zeros((m*m,n))

# Run the KF
j = 0
for Q in sigmas:
    for R in sigmas:
        for i in range(n): xhat[j,i], P = kf(xhat[j,i].flatten(), z[:,i], A, P, Q, R, H)
        j+=1

for i in range(m*m):
    plt.subplot(m,m,i+1)
    plt.plot(x,r,'r.')
    plt.plot(x,y,'k--')
    plt.plot(x,xhat[i,:],'g')
    # plt.title('Q = 1.0 and R = 1.0')

plt.show()
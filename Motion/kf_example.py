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

# Generate the points
n = 500
x = np.arange(0.,5.,5./n)
y = np.array(function(x))

# Added random noise
mu, sigma = 0, 0.2
s = np.random.normal(mu, sigma, n)
r = y + s

# Static elements of KF
z = r.reshape((n,1))
A = np.array([[1.0]])
P = np.array([[1.0]])
H = np.array([[1.0]])

# Variable elements of KF
xhat1, xhat2, xhat3 = np.zeros((n,1)), np.zeros((n,1)), np.zeros((n,1))
xhat4, xhat5, xhat6 = np.zeros((n,1)), np.zeros((n,1)), np.zeros((n,1))
xhat7, xhat8, xhat9 = np.zeros((n,1)), np.zeros((n,1)), np.zeros((n,1))
Q1, R1 = 0.1, 0.1
Q2, R1 = 0.5, 0.1
Q3, R1 = 1.0, 0.1
Q1, R2 = 0.1, 0.5
Q2, R2 = 0.5, 0.5
Q3, R2 = 1.0, 0.5
Q1, R3 = 0.1, 1.0
Q2, R3 = 0.5, 1.0
Q3, R3 = 1.0, 1.0

# Run the KF
for i in range(n): xhat1[i], P = kf(xhat1[i], z[i], A, P, Q1, R1, H)
for i in range(n): xhat2[i], P = kf(xhat2[i], z[i], A, P, Q2, R1, H)
for i in range(n): xhat3[i], P = kf(xhat3[i], z[i], A, P, Q3, R1, H)
for i in range(n): xhat4[i], P = kf(xhat4[i], z[i], A, P, Q1, R2, H)
for i in range(n): xhat5[i], P = kf(xhat5[i], z[i], A, P, Q2, R2, H)
for i in range(n): xhat6[i], P = kf(xhat6[i], z[i], A, P, Q3, R2, H)
for i in range(n): xhat7[i], P = kf(xhat7[i], z[i], A, P, Q1, R3, H)
for i in range(n): xhat8[i], P = kf(xhat8[i], z[i], A, P, Q2, R3, H)
for i in range(n): xhat9[i], P = kf(xhat9[i], z[i], A, P, Q3, R3, H)

# Plot the results
plt.subplot(3,3,1)
plt.plot(x,y,'k--')
plt.plot(x,r,'r.')
plt.plot(x,xhat1,'g')
plt.title('Q = 0.1 and R = 0.1')

plt.subplot(3,3,2)
plt.plot(x,y,'k--')
plt.plot(x,r,'r.')
plt.plot(x,xhat2,'g')
plt.title('Q = 0.5 and R = 0.1')

plt.subplot(3,3,3)
plt.plot(x,y,'k--')
plt.plot(x,r,'r.')
plt.plot(x,xhat3,'g')
plt.title('Q = 1.0 and R = 0.1')

plt.subplot(3,3,4)
plt.plot(x,y,'k--')
plt.plot(x,r,'r.')
plt.plot(x,xhat4,'g')
plt.title('Q = 0.1 and R = 0.5')

plt.subplot(3,3,5)
plt.plot(x,y,'k--')
plt.plot(x,r,'r.')
plt.plot(x,xhat5,'g')
plt.title('Q = 0.5 and R = 0.5')

plt.subplot(3,3,6)
plt.plot(x,y,'k--')
plt.plot(x,r,'r.')
plt.plot(x,xhat6,'g')
plt.title('Q = 1.0 and R = 0.5')

plt.subplot(3,3,7)
plt.plot(x,y,'k--')
plt.plot(x,r,'r.')
plt.plot(x,xhat7,'g')
plt.title('Q = 0.1 and R = 1.0')

plt.subplot(3,3,8)
plt.plot(x,y,'k--')
plt.plot(x,r,'r.')
plt.plot(x,xhat8,'g')
plt.title('Q = 0.5 and R = 1.0')

plt.subplot(3,3,9)
plt.plot(x,y,'k--')
plt.plot(x,r,'r.')
plt.plot(x,xhat9,'g')
plt.title('Q = 1.0 and R = 1.0')

plt.show()
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
    xhat.reshape((m,1))
    z.reshape((n,1))
    I = np.eye(m)
    # KF - Prediction
    xhat = np.dot(A, xhat)
    P    = np.dot(A, np.dot(P, A.T)) + Q
    # KF - Update
    S    = np.dot(H, np.dot(P, H.T)) + R
    K    = np.dot(P, np.dot(H.T, lin.inv(S)))
    v    = z - np.dot(H, xhat)
    xhat = xhat + np.dot(K, v)
    P    = np.dot((I - np.dot(K, H)), P)
    return xhat, P


def genData(x, w=None):
    if w is None:
        w = np.random.random([3])*2.0
    y = []
    [y.append( w[0]*np.sin(w[1]*x[i])*np.cos(w[2]*x[i]) ) for i in range(len(x))]
    return np.array(y)

# Generate the samples
n = 250
t = np.arange(0.,5.,5./n)
mx = genData(t)
my = genData(t)
mz = genData(t)

# Add random noise
mu, sigma = 0, 0.01
s = np.random.normal(mu, sigma, (3,n))
rx = mx + s[0,:]
ry = my + s[1,:]
rz = mz + s[2,:]
# Measurement vectors
z = np.vstack((rx, ry, rz))

# Elements of KF
A = np.eye(3)
P = np.eye(3)
# Covariances
sigma_Q = 0.5
sigma_R = 0.01
Q = np.eye(3)*sigma_Q
R = np.eye(3)*sigma_R
# Observation Matrix
H = np.eye(3)


m = np.shape(z)[0]
xhat = np.zeros((m,n))
# Kalman Filter
for i in range(n):
    xhat[:,i], P = kf(xhat[:,i], z[:,i], A, P, Q, R, H)

# Plot the Results
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig1 = plt.figure()
plt.subplot(3,1,1)
plt.plot(t,mx,'k--', t,rx,'r.', t,xhat[0,:],'b-')
plt.subplot(3,1,2)
plt.plot(t,my,'k--', t,ry,'r.', t,xhat[1,:],'b-')
plt.subplot(3,1,3)
plt.plot(t,mz,'k--', t,rz,'r.', t,xhat[2,:],'b-')

fig2 = plt.figure()
ax = fig2.gca(projection='3d')
ax.plot(mx, my, mz, c='k', label='Movement in 3D')
ax.scatter(rx, ry, rz, c='r')
ax.plot(xhat[0,:], xhat[1,:], xhat[2,:], c='b')

plt.show()
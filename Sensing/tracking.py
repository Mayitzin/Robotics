"""
These functions are intended to be useful for Tracking Applications.
They include Transformation Matrices, Kalman Filtering and Geometric
estimations.

For the KF the following parameters apply:

Dimensions:
    m is the number of elements in array xhat.
    n is the length of array z (number of signals to be filtered).

Inputs:
    xhat is an m-by-1 array that contains the state vector of length m.

    z is an n-by-1 array that contains the data retrieved by the sensors.

    A is the Transition Matrix of size m-by-m.

    P is the a priori Estimated Covariance Matrix of size m-by-m.

    Q is the Dynamic disturbance Covariance Matrix of size m-by-m.

    R is the Sensor Noise Covariance Matrix of size n-by-n. Its length is
    defined by the number of signals to filter. In this case 3 from the
    accelerometer and 3 from the gyroscope. Hint: Is a diagonal Matrix.

    H is the Measurement Matrix of size n-by-n.

Outputs:
    xhat is an m-by-1 vector that contains the filtered estimations.

    P is an m-by-m matrix of the filtered estimated Covariance matrix.
    - Note: S. Saerkka defines the Updated Covariance as P = P - K*S*K'.

For futher reference see:
    [1] Hartikainen, J and Solin, A. and Saerkka, S. Optimal Filtering
        with Kalman Filters and Smoothers: a Manual for the Matlab
        toolbox EKF/UKF. Technical Report. Aalto University. 2011.
    [2] Welch, G. and Bishop, G. An Introduction to the Kalman Filter.
        University of North Carolina at Chapel Hill. SIGGRAPH 2001.

History:
    12.11.2014. First collection of Functions.
    17.11.2014. Test functions added.
                Enable Debug mode as extra parameter.
                Function q2coord added.
    21.11.2014. Changed limit of chordal distance in test function.
    24.11.2014. Added test of Quaternions for a valid rotation R.

@author: Mario Garcia
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
    
    
def ekf(xhat, z, A, P, Q, R, H):
    """
    The Extended Kalman Filtering needs the specification of an f-function
    and an h-function to linearize them. Further development to automate them
    should be pursued.
    TODO:
    - Automated specification of f- and h-function.
    """
    m = len(xhat)
    n = len(z)
    I = np.eye(m)
    W = np.eye(np.shape(Q)[0])
    V = np.eye(np.shape(R)[0])
    # KF - Prediction
    xhat = ffunc(A, xhat)
    P    = np.dot(A, np.dot(P, A.T)) + np.dot(W, np.dot(Q, W.T))
    # KF - Update
    S    = np.dot(H, np.dot(P, H.T)) + np.dot(V, np.dot(R, V.T))
    K    = np.dot(P, np.dot(H.T, lin.inv(S)))
    v    = z.reshape((n,1)) - hfunc(xhat)
    xhat = xhat + np.dot(K, v)
    P    = np.dot((I - np.dot(K, H)), P)
    return xhat, P


def buildF(dt):
    """
    buildF creates the 9-by-9 Model matrix F for the Kalman Filtering.
    A sample rate dt (the inverse of the frequency) is used and a state vector
    xhat with 9 elements is assumed.
    """
    O3x3  = np.zeros((3,3))
    I3x3  = np.eye(3)
    Dt3x3 = I3x3 * dt
    return np.vstack(( np.hstack( (O3x3, I3x3, Dt3x3) ),
                       np.hstack( (O3x3, O3x3,  I3x3) ),
                       np.hstack( (O3x3, O3x3,  O3x3) ) ))


def buildA(dt):
    """
    buildA creates the 9-by-9 Transition matrix A for the Kalman Filtering.
    A sample rate dt (the inverse of the frequency) is used and a state vector
    xhat with 9 elements is assumed.
    """
    O3x3  = np.zeros((3,3))
    I3x3  = np.eye(3)
    Dt3x3 = I3x3 * dt
    Dt23x3= I3x3 * (0.5*dt**2)
    return np.vstack(( np.hstack( (I3x3, Dt3x3, Dt23x3) ),
                       np.hstack( (O3x3,  I3x3,  Dt3x3) ),
                       np.hstack( (O3x3,  O3x3,   I3x3) ) ))


def buildR(rc):
    """
    buildR creates the n-by-n Sensor Noise Covariance matrix R, given an
    n-vector _rc_ with the individual sensor variances.
    """
    return np.eye(len(rc)) * rc


def buildQ(qc,F,dt):
    """
    buildQ creates the 9-by-9 Process Noise matrix Q for the Kalman
    Filtering. A 9-vector qc with its noise parameters must be provided, as
    well as the 9-by-9 model matrix F.
    """
    m   = len(qc)
    Qc  = np.eye(m)*qc
    Phi = np.vstack((np.hstack((F, Qc)),np.hstack((np.zeros((m,m)),-F.T))))
    CD  = np.dot(lin.expm(np.dot(Phi,dt)),np.vstack((np.zeros((m,m)),np.eye(m))))
    return lin.solve(CD[m::,:],CD[0:m,:])



## TEST FUNCTIONS ##

# Format Output in Terminal (ANSI Escape Sequences)
class bcolors:
    HEAD = '\033[95m'       # Header (purple)
    ENBL = '\033[94m'       # Enabling a mode (Blue)
    OKGR = '\033[92m'       # OK message (Green)
    WARN = '\033[93m'       # Warning message (Yellow)
    FAIL = '\033[91m'       # FAIL message (Red)
    ENDC = '\033[0m'        # End formatting

# PENDING!!
# TODO: Test functions for the above script.


## MAIN EXECUTION as a script ##
if __name__ == "__main__":
    import sys
    
    # Default values
    dmode = False       # Debug mode is OFF

    # Read extra parameters (if given)
    if len(sys.argv) == 2:
        print "This script is not yet fully customizable"
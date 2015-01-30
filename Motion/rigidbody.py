"""
These functions are intended to be useful for the computation over Rigid
Body Motion. They include Transformation Matrices and Geometric
estimations.

For futher reference see:
    [1] Craig, J. Introduction to Robotics: Mechanics and Control. 3rd
        Edition. Pearson Education, pages 19-54. 2005.

History:
    12.11.2014. First collection of Functions.
    17.11.2014. Test functions added.
                Enable Debug mode as extra parameter.
    21.11.2014. Changed limit of chordal distance in test function.
    24.11.2014. Added test of Quaternions for a valid rotation R.
    28.01.2015. Separated from script "tracking.py".

@author: Mario Garcia
"""

import numpy as np
import scipy.linalg as lin
    
    
def rotate(ex,ey,ez):
    """
    This creates a 3-by-3 rotation matrix R in SO(3) with the common
    sequence xyz created by multiplying three rotation matrices of the
    form:
        R = Rz(ez)*Ry(ey)*Rx(ex)
    where ex, ey and ez are given in degrees.
    """
    # Convert from degrees to radians
    ex = float(ex)*np.pi/180
    ey = float(ey)*np.pi/180
    ez = float(ez)*np.pi/180
    # Build rotation matrices
    Rx = np.array([[1, 0, 0],[0, np.cos(ex), -np.sin(ex)],[0, np.sin(ex), np.cos(ex)]])
    Ry = np.array([[np.cos(ey), 0, np.sin(ey)],[0, 1, 0],[-np.sin(ey), 0, np.cos(ey)]])
    Rz = np.array([[np.cos(ez), -np.sin(ez), 0],[np.sin(ez), np.cos(ez), 0],[0, 0, 1]])
    return np.dot(Rz,np.dot(Ry,Rx))


def initpose(acx, acy, acz):
    """
    initpose naively computes the pose of the pen based SOLELY on the
    acceleration forces sensed along each axis.
    NOTE: Still in development.
    """
    # Get norm of acceleration vector
    acn = np.sqrt(acx**2 + acy**2 + acz**2)
    # Normalize values
    acx /= acn
    acy /= acn
    acz /= acn
    # Estimate X and Y angles
    ex = np.arctan2( acy, acz) * 180/np.pi
    ey = np.arctan2(-acx, np.sqrt(acy**2 + acz**2)) * 180/np.pi
    ez = 0
    return np.vstack((ex,ey,ez))


def q2R(q=[1,0,0,0]):
    """
    q2R builds a rotation matrix R in SO(3) from a given Quaternion q of
    the form q = [q_w, q_x, q_y, q_z].
    The default value is the Quaternion q=[1,0,0,0] that produces a
    3-by-3 Identity matrix.
    """
    return np.array([
        [  1-2*(q[2]**2+q[3]**2),    2*(q[1]*q[2]-q[0]*q[3]),  2*(q[1]*q[3]+q[0]*q[2])  ],
        [  2*(q[1]*q[2]+q[0]*q[3]),  1-2*(q[1]**2+q[3]**2),    2*(q[2]*q[3]-q[0]*q[1])  ],
        [  2*(q[1]*q[3]-q[0]*q[2]),  2*(q[0]*q[1]+q[2]*q[3]),  1-2*(q[1]**2+q[2]**2)    ]])


def hmtrans(R,t):
    """
    hmtrans build the 4-by-4 homogeneous transformation matrix of the form:
        T = | R t |
            | 0 1 |
    where R is a 3-by-3 rotation matrix and t is the 3-translation vector.
    """
    T = np.vstack((np.hstack((R,t)),np.array([0,0,0,1])))
    return  T.astype(np.float)


def dchord(R1,R2):
    """
    dchord computes the chordal distance between two rotation matrices
    R1 and R2. Possible outputs are:
    - It is equal to zero if both matrices are equal.
    - It is equal to sqrt(12) ~ 3.464 if they are completely different.
    """
    A = R1 - R2
    return np.sqrt(np.trace(np.dot(A.T, A)))


def invTrans(T):
    """
    invTrans computes the inverse 4-by-4 homogeneous transformation of T,
    whose output is of the form:
        T^-1 = | R^T  -R^T*t |
               |  0      1   |
    """
    R = T[0:3,0:3]
    t = np.vstack(T[0:3,3])
    return np.vstack((np.hstack(( R.T, np.dot(-R.T,t))), np.array([0,0,0,1])))



## TEST FUNCTIONS ##

# Format Output in Terminal (ANSI Escape Sequences)
class bcolors:
    HEAD = '\033[95m'       # Header (purple)
    ENBL = '\033[94m'       # Enabling a mode (Blue)
    OKGR = '\033[92m'       # OK message (Green)
    WARN = '\033[93m'       # Warning message (Yellow)
    FAIL = '\033[91m'       # FAIL message (Red)
    ENDC = '\033[0m'        # End formatting


def test_Rotation(space='Euler',debug=False):
    """
    This function test whether the inner functions "rotate" and q2R are
    able to build a valid rotation matrix. Two types of parameters can be
    used to construct a rotation matrix: Euler angles and Quaternions.
    - Default space is 'Euler'. It generates 3 random values from -180 to
      +180 degrees as inputs to create a rotation matrix R.
    - The second method to test is 'Quat'. It generates 4 random values
      of a unitary quaternion and they are used with the function q2R to
      build the rotation matrix R.
    Both methods must produce a valid rotation matrix, which is tested
    in this function.
    """
    if space=='Euler':
        angs = np.random.random(3)*360-180                  # 3 Random angles from -180 to +180
        R    = rotate(angs[0], angs[1], angs[2])            # Rotation matrix R from 3 random angles
        detR = lin.det(R)                                   # Determinant of R
        if debug:
            # Print the used angles and the determinant of the rotation matrix if Debug mode is ON
            print "----------------------------------------------------------------------"
            print " ex = %3.4f \n ey = %3.4f \n ez = %3.4f" % (angs[0], angs[1], angs[2])
            print " det(R) = %1.4f" % detR
    elif space=='Quat':
        q    = np.random.random(4)                          # 4 random values of q
        qn   = np.sqrt(q[0]**2+q[1]**2+q[2]**2+q[3]**2)     # Euclidean length
        q   /= qn                                           # Normalization of vector
        R    = q2R(q)                                       # Rotation matrix R from unitary quaternion
        detR = lin.det(R)                                   # Determinant of R
        if debug:
            # Print the used quaternion and the determinant of the rotation matrix if Debug mode is ON
            print "----------------------------------------------------------------------"
            print " q_w = %1.4f \n q_x = %1.4f \n q_y = %1.4f \n q_z = %1.4f" % (q[0],q[1],q[2],q[3])
            print " det(R) = %1.4f" % detR
    # Test if det(R)=+1 and R^T*R=I
    if ((detR-1.0) < 1e-9) and ((np.trace(np.dot(R.T, R))-3.0) < 1e-9):
        print "- Valid construction of rotation matrix ................ [",bcolors.OKGR+"OK"+bcolors.ENDC,"]"
    else:
        print "- Valid construction of rotation matrix ................ [",bcolors.FAIL+"NO"+bcolors.ENDC,"]"


def test_ChordalDist(debug=False):
    """
    This function tests if two rotation matrices have a valid chordal
    distance (measurable in SO(3)) as defined by Hartley et.al. (2013).
    """
    # Create first rotation with Euler angles
    ang = np.random.random(3)*360-180                  # 3 Random angles from -180 to +180
    R1  = rotate(ang[0], ang[1], ang[2])               # Rotation matrix R of the 3 random angles
    # Create second rotation with Quaternions
    q   = np.random.random(4)                          # 4 random values of q
    qn  = np.sqrt(q[0]**2+q[1]**2+q[2]**2+q[3]**2)     # Euclidean length of q
    q  /= qn                                           # Normalization of vector
    R2  = q2R(q)                                       # Rotation matrix R from unitary quaternion
    d   = dchord(R1,R2)                                # Chordal distance
    if debug:
        # Printed the used angles, rotations, and thir chordal distance
        print "----------------------------------------------------------------------"
        print "Euler_angles     =", ang, "\nRotation_1:\n", R1
        print "Unit_Quaternion  =", q,   "\nRotation_2:\n", R2
        print "Chordal distance =", d
    # Test if Chordal distance is within the valid range
    if 0.0 <= d:
        print "- Valid distance between two rotation matrices ......... [",bcolors.OKGR+"OK"+bcolors.ENDC,"]"
    else:
        print "- Valid distance between two rotation matrices ......... [",bcolors.FAIL+"NO"+bcolors.ENDC,"]"


## MAIN EXECUTION as a script ##
if __name__ == "__main__":
    import sys
    
    # Default values
    dmode = False       # Debug mode is OFF
    smode = 'Quat'      # Space mode is 'Quaternions'

    # Read extra parameters (if given)
    if len(sys.argv) == 2:
        mode = sys.argv[1]
        if mode == "--debug":
            dmode = True
            print bcolors.ENBL+"Debug mode is ON"+bcolors.ENDC
        else:
            print bcolors.WARN+"Given parameter is not valid.\nProceeding with default values."+bcolors.ENDC

    # Start Running Tests in given mode
    print "Running tests... "
    test_Rotation(space=smode, debug=dmode)
    test_ChordalDist(debug=dmode)
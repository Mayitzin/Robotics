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
    19.03.2016. Added Madwicks' Algorithm.
    27.07.2018. Modified Madgwick's Algorithm and initial pose estimation.
                Add cosine and sine functions for degrees.

@author: Mario Garcia
"""

import numpy as np
import scipy.linalg as lin
import platform

# Check OS
LINUX = platform.system() == 'Linux'

# Default values
rad2deg = 180.0/np.pi
deg2rad = np.pi/180.0
default_freq = 100.0


def cosd(deg):
    return np.cos(deg*deg2rad)


def sind(deg):
    return np.sin(deg*deg2rad)


def rotate(ex,ey,ez):
    """rotate creates a 3-by-3 rotation matrix R in SO(3) with the common
    sequence xyz created by multiplying three rotation matrices of the form:
        R = Rz(ez)*Ry(ey)*Rx(ex)
    where ex, ey and ez are given in degrees.
    """
    # Convert from degrees to radians
    ex *= deg2rad
    ey *= deg2rad
    ez *= deg2rad
    # Build rotation matrices
    Rx = np.array([[1, 0, 0],[0, np.cos(ex), -np.sin(ex)],[0, np.sin(ex), np.cos(ex)]])
    Ry = np.array([[np.cos(ey), 0, np.sin(ey)],[0, 1, 0],[-np.sin(ey), 0, np.cos(ey)]])
    Rz = np.array([[np.cos(ez), -np.sin(ez), 0],[np.sin(ez), np.cos(ez), 0],[0, 0, 1]])
    return np.dot(Rz,np.dot(Ry,Rx))


def am2q(a=[], m=[], retype='q'):
    """am2q naively computes the pose of the pen based on the acceleration
    forces sensed along each axis. Additionally, a triaxial magnetometer can be
    used.
    """
    acx, acy, acz = a[0], a[1], a[2]
    # Get norm of acceleration vector
    acn = np.sqrt(acx**2 + acy**2 + acz**2)
    # Normalize values
    acx /= acn
    acy /= acn
    acz /= acn
    # Estimate Roll and Pitch angles (Yaw is equal to Zero)
    ex = np.arctan2( acy, acz)
    ey = np.arctan2(-acx, np.sqrt(acy**2 + acz**2))
    ez = 0
    # Euler to Quaternion
    cx2 = np.cos(ex/2.0)
    sx2 = np.sin(ex/2.0)
    cy2 = np.cos(ey/2.0)
    sy2 = np.sin(ey/2.0)
    qrw =  cx2*cy2
    qrx =  sx2*cy2
    qry =  cx2*sy2
    qrz = -sx2*sy2
    # Normalize reference Quaternion
    invsqrt = np.sqrt(qrw**2 + qrx**2 + qry**2 + qrz**2)
    qw = qrw / invsqrt
    qx = qrx / invsqrt
    qy = qry / invsqrt
    qz = qrz / invsqrt
    # Compass values were also provided (to get heading value)
    if len(m)>2:
        mx, my, mz = m[0], m[1], m[2]
        # Normalize magnetometer measurements
        invsqrt = np.sqrt(mx**2 + my**2 + mz**2)
        mx /= invsqrt
        my /= invsqrt
        mz /= invsqrt
        # Auxiliary variables to save computation
        qw2 = qw*qw
        qx2 = qx*qx
        qy2 = qy*qy
        qz2 = qz*qz
        # Quaternion vector product = qr x (qm x qr*)  = qprod(r, qprod(m,qconj(r)) )
        qmx =     mx*(qw2 + qx2 - qy2 - qz2) - 2.0*my*(qw*qz - qx*qy)         + 2.0*mz*(qw*qy + qx*qz)
        qmy = 2.0*mx*(qw*qz + qx*qy)         +     my*(qw2 - qx2 + qy2 - qz2) + 2.0*mz*(qy*qz - qw*qx)
        # Estimate Yaw
        ez = np.arctan2(-qmy, qmx)
        # Build final Quaternion
        cz2 = np.cos(ez/2.0)
        sz2 = np.sin(ez/2.0)
        qw = cx2*cy2*cz2 + sx2*sy2*sz2
        qx = sx2*cy2*cz2 - cx2*sy2*sz2
        qy = cx2*sy2*cz2 + sx2*cy2*sz2
        qz = cx2*cy2*sz2 - sx2*sy2*cz2
        # Normalize quaternion
        invsqrt = np.sqrt(qw**2 + qx**2 + qy**2 + qz**2)
        qw /= invsqrt
        qx /= invsqrt
        qy /= invsqrt
        qz /= invsqrt
    # Return desired values (Quaterion or Euler Angles)
    if retype=='q':
        return [qw, qx, qy, qz]
    else:
        # Convert Radians to Euler Angles
        ex *= rad2deg
        ey *= rad2deg
        ez *= rad2deg
        return [ex, ey, ez]


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


class Quaternion:
    def __init__(self, quaternion=[1.0, 0.0, 0.0, 0.0]):
        self.q = quaternion

    def normalize(self, q):
        return q / np.linalg.norm(q)

    def q2R(self, q):
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


class Mahony:
    def updateIMU(acc, gyr, q=[1.0,0.0,0.0,0.0], freq=default_freq, Kp=0.1, Ki=0.5):
        """Mahony's AHRS algorithm with an IMU architecture.

        Adapted to Python from original implementation by Sebastian Madgwick.

        See: "Nonlinear Complementary Filters on the Special Orthogonal Group"
             https://hal.archives-ouvertes.fr/hal-00488376/document
        See: http://www.x-io.co.uk/open-source-imu-and-ahrs-algorithms/
        See: http://www.olliw.eu/2013/imu-data-fusing/
        """
        twoKp = 2.0*Kp     # 2 * proportional gain
        twoKi = 2.0*Ki     # 2 * integral gain
        integralFBx = 0.0
        integralFBy = 0.0
        integralFBz = 0.0
        # Get elements from input
        ax, ay, az = acc[0], acc[1], acc[2]
        gx, gy, gz = gyr[0], gyr[1], gyr[2]
        qw, qx, qy, qz = q[0], q[1], q[2], q[3]
        # Compute feedback only if accelerometer measurement valid
        # (avoids NaN in accelerometer normalisation)
        if( not((ax==0.0) & (ay==0.0) & (az==0.0)) ):
            # Normalise accelerometer measurement
            recipNorm = np.sqrt(ax * ax + ay * ay + az * az)
            ax /= recipNorm
            ay /= recipNorm
            az /= recipNorm
            # Estimated direction of gravity
            halfvx = qx*qz - qw*qy
            halfvy = qw*qx + qy*qz
            halfvz = qw*qw + qz*qz - 0.5
            # Error is sum of cross product between estimated
            # and measured direction of gravity
            halfex = (ay * halfvz - az * halfvy)
            halfey = (az * halfvx - ax * halfvz)
            halfez = (ax * halfvy - ay * halfvx)
            # Compute and apply integral feedback if enabled
            if(twoKi > 0.0):
                # integral error scaled by Ki
                integralFBx += twoKi * halfex / freq
                integralFBy += twoKi * halfey / freq
                integralFBz += twoKi * halfez / freq
                # apply integral feedback
                gx += integralFBx
                gy += integralFBy
                gz += integralFBz
            else:
                # prevent integral windup
                integralFBx = 0.0
                integralFBy = 0.0
                integralFBz = 0.0
            # Apply proportional feedback
            gx += twoKp * halfex
            gy += twoKp * halfey
            gz += twoKp * halfez
        # Integrate rate of change of quaternion
        gx *= (0.5 / freq)       # pre-multiply common factors
        gy *= (0.5 / freq)
        gz *= (0.5 / freq)
        qa = qw
        qb = qx
        qc = qy
        qw += (-qb * gx - qc * gy - qz * gz)
        qx += ( qa * gx + qc * gz - qz * gy)
        qy += ( qa * gy - qb * gz + qz * gx)
        qz += ( qa * gz + qb * gy - qc * gx)
        # Normalise quaternion
        recipNorm = np.sqrt(qw * qw + qx * qx + qy * qy + qz * qz)
        qw /= recipNorm
        qx /= recipNorm
        qy /= recipNorm
        qz /= recipNorm
        return [qw, qx, qy, qz]

    def updateMARG(acc, gyr, mag, q=[1.0,0.0,0.0,0.0], freq=default_freq, Kp=0.1, Ki=0.5):
        """Mahony's AHRS algorithm with a MARG architecture.

        Adapted to Python from original implementation by Sebastian Madgwick.

        See: http://www.x-io.co.uk/open-source-imu-and-ahrs-algorithms/
        See: "Nonlinear Complementary Filters on the Special Orthogonal Group"
             https://hal.archives-ouvertes.fr/hal-00488376/document
        See: http://www.olliw.eu/2013/imu-data-fusing/
        """
        twoKp = 2.0*Kp     # 2 * proportional gain
        twoKi = 2.0*Ki     # 2 * integral gain
        integralFBx = 0.0
        integralFBy = 0.0
        integralFBz = 0.0
        # Get elements from input
        ax, ay, az = acc[0], acc[1], acc[2]
        gx, gy, gz = gyr[0], gyr[1], gyr[2]
        mx, my, mz = mag[0], mag[1], mag[2]
        q0, q1, q2, q3 = q[0], q[1], q[2], q[3]
        # Use IMU algorithm if magnetometer measurement invalid (avoids NaN in magnetometer normalisation)
        if( (mx==0.0) & (my==0.0) & (mz==0.0) ):
            Mahony.updateIMU(acc, gyr, q, freq, Kp, Ki)
        # Compute feedback only if accelerometer measurement valid (avoids NaN in accelerometer normalisation)
        if( not((ax==0.0) & (ay==0.0) & (az==0.0)) ):
            # Normalise accelerometer measurement
            recipNorm = np.sqrt(ax * ax + ay * ay + az * az)
            ax /= recipNorm
            ay /= recipNorm
            az /= recipNorm
            # Normalise magnetometer measurement
            recipNorm = np.sqrt(mx * mx + my * my + mz * mz)
            mx /= recipNorm
            my /= recipNorm
            mz /= recipNorm
            # Auxiliary variables to avoid repeated arithmetic
            q0q0 = q0 * q0
            q0q1 = q0 * q1
            q0q2 = q0 * q2
            q0q3 = q0 * q3
            q1q1 = q1 * q1
            q1q2 = q1 * q2
            q1q3 = q1 * q3
            q2q2 = q2 * q2
            q2q3 = q2 * q3
            q3q3 = q3 * q3
            # Reference direction of Earth's magnetic field
            hx = 2.0 * (mx * (0.5 - q2q2 - q3q3) + my * (q1q2 - q0q3) + mz * (q1q3 + q0q2))
            hy = 2.0 * (mx * (q1q2 + q0q3) + my * (0.5 - q1q1 - q3q3) + mz * (q2q3 - q0q1))
            bx = np.sqrt(hx * hx + hy * hy)
            bz = 2.0 * (mx * (q1q3 - q0q2) + my * (q2q3 + q0q1) + mz * (0.5 - q1q1 - q2q2))
            # Estimated direction of gravity and magnetic field
            halfvx = q1q3 - q0q2
            halfvy = q0q1 + q2q3
            halfvz = q0q0 - 0.5 + q3q3
            halfwx = bx * (0.5 - q2q2 - q3q3) + bz * (q1q3 - q0q2)
            halfwy = bx * (q1q2 - q0q3) + bz * (q0q1 + q2q3)
            halfwz = bx * (q0q2 + q1q3) + bz * (0.5 - q1q1 - q2q2)
            # Error is sum of cross product between estimated direction and measured direction of field vectors
            halfex = (ay * halfvz - az * halfvy) + (my * halfwz - mz * halfwy)
            halfey = (az * halfvx - ax * halfvz) + (mz * halfwx - mx * halfwz)
            halfez = (ax * halfvy - ay * halfvx) + (mx * halfwy - my * halfwx)
            # Compute and apply integral feedback if enabled
            if(twoKi > 0.0) :
                integralFBx += twoKi * halfex / freq    # integral error scaled by Ki
                integralFBy += twoKi * halfey / freq
                integralFBz += twoKi * halfez / freq
                gx += integralFBx  # apply integral feedback
                gy += integralFBy
                gz += integralFBz
            else:
                integralFBx = 0.0 # prevent integral windup
                integralFBy = 0.0
                integralFBz = 0.0
            # Apply proportional feedback
            gx += twoKp * halfex
            gy += twoKp * halfey
            gz += twoKp * halfez
        
        # Integrate rate of change of quaternion
        gx *= (0.5 / freq)     # pre-multiply common factors
        gy *= (0.5 / freq)
        gz *= (0.5 / freq)
        qa = q0
        qb = q1
        qc = q2
        q0 += (-qb * gx - qc * gy - q3 * gz)
        q1 += ( qa * gx + qc * gz - q3 * gy)
        q2 += ( qa * gy - qb * gz + q3 * gx)
        q3 += ( qa * gz + qb * gy - qc * gx)
        # Normalise quaternion
        recipNorm = np.sqrt(q0 * q0 + q1 * q1 + q2 * q2 + q3 * q3)
        q0 /= recipNorm
        q1 /= recipNorm
        q2 /= recipNorm
        q3 /= recipNorm
        q_array = [q0, q1, q2, q3]
        return q_array


class Madgwick:
    def updateIMU(acc, gyr, q=np.array([1.0,0.0,0.0,0.0]), beta=0.01, freq=100.0):
        # Get elements from input
        ax, ay, az = acc[0], acc[1], acc[2]
        gx, gy, gz = gyr[0], gyr[1], gyr[2]
        qw, qx, qy, qz = q[0], q[1], q[2], q[3]
        sampleFreq = freq
        # Rate of change of quaternion from gyroscope
        qDot1 = 0.5 * (-qx*gx - qy*gy - qz*gz)
        qDot2 = 0.5 * ( qw*gx + qy*gz - qz*gy)
        qDot3 = 0.5 * ( qw*gy - qx*gz + qz*gx)
        qDot4 = 0.5 * ( qw*gz + qx*gy - qy*gx)
        # Compute feedback only if accelerometer measurement valid (avoids NaN in accelerometer normalisation)
        if( not((ax==0.0) & (ay==0.0) & (az==0.0)) ):
            # Normalise accelerometer measurement
            recipNorm = np.sqrt(ax * ax + ay * ay + az * az)
            ax /= recipNorm
            ay /= recipNorm
            az /= recipNorm
            # Auxiliary variables to avoid repeated arithmetic
            qwqw = qw * qw
            qxqx = qx * qx
            qyqy = qy * qy
            qzqz = qz * qz
            qx_qy = qxqx + qyqy
            # Gradient decent algorithm corrective step
            s0 = 2.0*( qy*ax - qx*ay) + 4.0*qw*qx_qy
            s1 = 2.0*(-qz*ax - qw*ay) + 4.0*qx*(qwqw + qzqz + az - 1.0) + 8.0*qx*qx_qy
            s2 = 2.0*( qw*ax - qz*ay) + 4.0*qy*(qwqw + qzqz + az - 1.0) + 8.0*qy*qx_qy
            s3 = 2.0*(-qx*ax - qy*ay) + 4.0*qz*qx_qy
            # normalise step magnitude
            recipNorm = np.sqrt(s0 * s0 + s1 * s1 + s2 * s2 + s3 * s3)
            s0 /= recipNorm
            s1 /= recipNorm
            s2 /= recipNorm
            s3 /= recipNorm
            # Apply feedback step
            qDot1 -= beta * s0
            qDot2 -= beta * s1
            qDot3 -= beta * s2
            qDot4 -= beta * s3
        # Integrate rate of change of quaternion to yield quaternion
        qw += qDot1 / sampleFreq
        qx += qDot2 / sampleFreq
        qy += qDot3 / sampleFreq
        qz += qDot4 / sampleFreq
        # Normalise quaternion
        recipNorm = np.sqrt(qw * qw + qx * qx + qy * qy + qz * qz)
        qw /= recipNorm
        qx /= recipNorm
        qy /= recipNorm
        qz /= recipNorm
        return [qw, qx, qy, qz]

    def updateMARG(acc, gyr, mag, q=np.array([1.0,0.0,0.0,0.0]), beta=0.01, freq=100.0):
        """Madgwick's AHRS algorithm with a MARG architecture.

        Adapted to Python from original implementation by Sebastian Madgwick.

        See: http://www.x-io.co.uk/open-source-imu-and-ahrs-algorithms/
        @author: Sebastian Madgwick (2011)
        See: http://www.olliw.eu/2013/imu-data-fusing/
        """
        # Get elements from input
        ax, ay, az = acc[0], acc[1], acc[2]
        gx, gy, gz = gyr[0], gyr[1], gyr[2]
        mx, my, mz = mag[0], mag[1], mag[2]
        qw, qx, qy, qz = q[0], q[1], q[2], q[3]
        sampleFreq = freq
        # Rate of change of quaternion from gyroscope
        qDot1 = 0.5*(-qx*gx - qy*gy - qz*gz)
        qDot2 = 0.5*( qw*gx + qy*gz - qz*gy)
        qDot3 = 0.5*( qw*gy - qx*gz + qz*gx)
        qDot4 = 0.5*( qw*gz + qx*gy - qy*gx)
        # Compute feedback only if accelerometer measurement valid (avoids unvalid accelerometer values)
        if( not((ax==0.0) & (ay==0.0) & (az==0.0)) ):
            # Normalize accelerometers measurement
            invsqrt = np.sqrt(ax*ax + ay*ay + az*az)
            ax /= invsqrt
            ay /= invsqrt
            az /= invsqrt
            # Normalize magnetometers measurement
            invsqrt = np.sqrt(mx*mx + my*my + mz*mz)
            mx /= invsqrt
            my /= invsqrt
            mz /= invsqrt
            # Auxiliary variables to avoid repeated arithmetic
            qwqw = qw*qw
            qwqx = qw*qx
            qwqy = qw*qy
            qwqz = qw*qz
            qxqx = qx*qx
            qxqy = qx*qy
            qxqz = qx*qz
            qyqy = qy*qy
            qyqz = qy*qz
            qzqz = qz*qz
            _2qwqy = 2.0*qwqy
            _2qyqz = 2.0*qyqz
            # Reference direction of Earth's magnetic field
            hx     =      mx*(qwqw + qxqx - qyqy - qzqz)  - 2.0*my*(qwqz - qxqy)               + 2.0*mz*(qwqy + qxqz)
            hy     =  2.0*mx*(qwqz + qxqy)                +     my*(qwqw - qxqx + qyqy - qzqz) - 2.0*mz*(qwqx - qyqz)
            hz     = -2.0*mx*(qwqy - qxqz)                + 2.0*my*(qwqx + qyqz)               +     mz*(qwqw - qxqx - qyqy + qzqz)
            hxhy   = np.sqrt(hx*hx + hy*hy)
            _2hxhy = 2.0*hxhy
            _2hz   = 2.0*hz
            _2qax  = 2.0*qxqz - _2qwqy - ax
            _2qay  = 2.0*qwqx + _2qyqz - ay
            _4qaz  = 4.0*(1.0 - 2.0*qxqx - 2.0*qyqy - az)
            sumx = hxhy*(0.5 - qyqy - qzqz)  + hz*(qxqz - qwqy)       - mx
            sumy = hxhy*(qxqy - qwqz)        + hz*(qwqx + qyqz)       - my
            sumz = hxhy*(qwqy + qxqz)        + hz*(0.5 - qxqx - qyqy) - mz
            # Gradient decent algorithm corrective step
            s0 = 2.0*(-qy*_2qax + qx*_2qay)            - sumx*hz*qy                + sumy*(-hxhy*qz + hz*qx) + sumz*hxhy*qy
            s1 = 2.0*( qz*_2qax + qw*_2qay) - qx*_4qaz + sumx*hz*qz                + sumy*( hxhy*qy + hz*qw) + sumz*(hxhy*qz - _2hz*qx)
            s2 = 2.0*(-qw*_2qax + qz*_2qay) - qy*_4qaz - sumx*( _2hxhy*qy + hz*qw) + sumy*( hxhy*qx + hz*qz) + sumz*(hxhy*qw - _2hz*qy)
            s3 = 2.0*( qx*_2qax + qy*_2qay)            + sumx*(-_2hxhy*qz + hz*qx) + sumy*(-hxhy*qw + hz*qy) + sumz*hxhy*qx
            # normalize step magnitude
            invsqrt = np.sqrt(s0*s0 + s1*s1 + s2*s2 + s3*s3)
            s0 /= invsqrt
            s1 /= invsqrt
            s2 /= invsqrt
            s3 /= invsqrt
            # Apply feedback step
            qDot1 -= beta*s0
            qDot2 -= beta*s1
            qDot3 -= beta*s2
            qDot4 -= beta*s3
        # Integrate rate of change of quaternion to yield quaternion
        qw += qDot1 / sampleFreq
        qx += qDot2 / sampleFreq
        qy += qDot3 / sampleFreq
        qz += qDot4 / sampleFreq
        # Normalize quaternion
        invsqrt = np.sqrt(qw*qw + qx*qx + qy*qy + qz*qz)
        qw /= invsqrt
        qx /= invsqrt
        qy /= invsqrt
        qz /= invsqrt
        # Return Numpy Array of updated Quaternion
        return [qw, qx, qy, qz]


## TEST FUNCTIONS ##

# Format Output in Terminal (ANSI Escape Sequences)
class Texter:
    HEAD = '\033[95m' if LINUX else '' # Header (purple)
    ENBL = '\033[94m' if LINUX else '' # Enabling a mode (Blue)
    OKGR = '\033[92m' if LINUX else '' # OK message (Green)
    WARN = '\033[93m' if LINUX else '' # Warning message (Yellow)
    FAIL = '\033[91m' if LINUX else '' # FAIL message (Red)
    ENDC = '\033[0m'  if LINUX else '' # End formatting

    MSG_OK = OKGR+"OK"+ENDC
    MSG_NO = FAIL+"NO"+ENDC

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
            print("----------------------------------------------------------------------")
            print(" ex = %3.4f \n ey = %3.4f \n ez = %3.4f" % (angs[0], angs[1], angs[2]))
            print(" det(R) = %1.4f" % detR)
    elif space=='Quat':
        q    = np.random.random(4)                          # 4 random values of q
        qn   = np.sqrt(q[0]**2+q[1]**2+q[2]**2+q[3]**2)     # Euclidean length
        q   /= qn                                           # Normalization of vector
        R    = q2R(q)                                       # Rotation matrix R from unitary quaternion
        detR = lin.det(R)                                   # Determinant of R
        if debug:
            # Print the used quaternion and the determinant of the rotation matrix if Debug mode is ON
            print("----------------------------------------------------------------------")
            print(" q_w = %1.4f \n q_x = %1.4f \n q_y = %1.4f \n q_z = %1.4f" % (q[0],q[1],q[2],q[3]))
            print(" det(R) = %1.4f" % detR)
    # Test if det(R)=+1 and R^T*R=I
    if ((detR-1.0) < 1e-9) and ((np.trace(np.dot(R.T, R))-3.0) < 1e-9):
        print("- Valid construction of rotation matrix ................ [",Texter.MSG_OK,"]")
    else:
        print("- Valid construction of rotation matrix ................ [",Texter.MSG_NO,"]")


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
        print("----------------------------------------------------------------------")
        print("Euler_angles     =", ang, "\nRotation_1:\n", R1)
        print("Unit_Quaternion  =", q,   "\nRotation_2:\n", R2)
        print("Chordal distance =", d)
    # Test if Chordal distance is within the valid range
    if 0.0 <= d:
        print("- Valid distance between two rotation matrices ......... [",Texter.MSG_OK,"]")
    else:
        print("- Valid distance between two rotation matrices ......... [",Texter.MSG_NO,"]")


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
            print(Texter.ENBL+"Debug mode is ON"+Texter.ENDC)
        else:
            print(Texter.WARN+"Given parameter is not valid.\nProceeding with default values."+Texter.ENDC)

    # Start Running Tests in given mode
    print("Running tests... ")
    test_Rotation(space=smode, debug=dmode)
    test_ChordalDist(debug=dmode)
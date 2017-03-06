"""
Tracking a sensor frame in 3D

@author: Mario Garcia
www.mayitzin.com
"""

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys


def q2R(q=[1,0,0,0]):
    """
    q2R builds a rotation matrix R in SO(3) from a given Quaternion q of the
    form q = [q_w, q_x, q_y, q_z].
    The default value is the Quaternion q=[1,0,0,0] that produces a 3-by-3
    Identity matrix.
    """
    return np.array([
        [  1-2*(q[2]**2+q[3]**2),    2*(q[1]*q[2]-q[0]*q[3]),  2*(q[1]*q[3]+q[0]*q[2])  ],
        [  2*(q[1]*q[2]+q[0]*q[3]),  1-2*(q[1]**2+q[3]**2),    2*(q[2]*q[3]-q[0]*q[1])  ],
        [  2*(q[1]*q[3]-q[0]*q[2]),  2*(q[0]*q[1]+q[2]*q[3]),  1-2*(q[1]**2+q[2]**2)    ]])


fileName = "./quaternions.csv"
freq = 100

if len(sys.argv)>1:
    fileName = sys.argv[1]
print "Using File:", fileName

# Read CSV File
with open(fileName, 'r') as f:
    data = f.readlines()

# Organize Quaternions into a numpy array
all_data = []
[all_data.append( i.strip().split(';') ) for i in data]
all_data = np.array(all_data, dtype='float')
m = np.shape(all_data)[0]  # Number of Samples
n = np.shape(all_data)[1]  # Number of Headers

########## Setuup Plotting Window ##########
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 0.1
w.setWindowTitle('Tracking movement from Quaternions')

# Add a grid on the Z-plane
gz = gl.GLGridItem()
gz.translate(0, 0, -0.1)
w.addItem(gz)

# Draw Frames
pltx = gl.GLLinePlotItem(pos=np.vstack(([0,0,0], [1,0,0])), color=np.array((1.0,0.0,0.0,1.0)), width=2., antialias=False)
plty = gl.GLLinePlotItem(pos=np.vstack(([0,0,0], [0,1,0])), color=np.array((0.0,1.0,0.0,1.0)), width=2., antialias=False)
pltz = gl.GLLinePlotItem(pos=np.vstack(([0,0,0], [0,0,1])), color=np.array((0.0,0.0,1.0,1.0)), width=2., antialias=False)
# Show lines
w.addItem(pltx)
w.addItem(plty)
w.addItem(pltz)
w.show()

i = 0
def update():
    global i
    R = q2R(q[i])
    pltx.setData( pos=np.vstack(( [0,0,0],  R[0:3,0] )))    # X-axis
    plty.setData( pos=np.vstack(( [0,0,0],  R[0:3,1] )))    # Y-axis
    pltz.setData( pos=np.vstack(( [0,0,0],  R[0:3,2] )))    # Z-axis
    if i<m-1:
        i += 1
    else:
        i=0
    txt = "\r%3.3f s\tq = [%f\t%f\t%f\t%f]"%(i/freq, q[i][0], q[i][1], q[i][2], q[i][3])
    sys.stdout.write(txt)
    sys.stdout.flush()


t = QtCore.QTimer()
t.timeout.connect(update)
t.start(1000/freq)     # Restarts timer every given interval (in miliseconds)


if __name__ == '__main__':
    ## Start Qt event loop unless running in interactive mode.
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

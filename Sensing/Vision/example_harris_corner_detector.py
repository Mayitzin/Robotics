# -*- coding: utf-8 -*-
"""
Breakdown of the Harris Corner detector.

This code plots each step estimating the corners in an image using the original
"Harris Corner Detector" Algorithm. See [2].

For futher reference see:
    [1] Foerstner, W. A feature-based correspondence algorithm for image
        matching. Intl. Arch. Photogrammetry & Remote Sensing,
        26(3):150–166. 1986
    [2] C. Harris and M.J. Stephens. A combined corner and edge detector.
        Alvey Vision Conference, pages 147–152, 1988.
    [3] Szeliski, R. Computer Vision: Algorithms and Applications.
        Springer, pages 212-214. 2010.
    [4] Prince, S.J.D. Computer Vision Models, Learning and Inference.
        Cambridge University Press. Pag. 339. 2012.

History:
    26.06.2015. First Implementation.
    28.06.2015. Added Sub-Plot.
    03.07.2015. Structure Tensor built.
                Simplified algorithm.
                Added References, and coding settings.
    07.07.2015. Detection of working OS.
                Conversion from RGB to grayscale now conforms CIE 1931.
    09.07.2015. Changed derivative mask to suggested by Harris and Stephens.
                Using notation of Prewitt/Sobel operators.

@author: Mario Garcia
www.mayitzin.com
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.ndimage as scimg
import numpy as np
import platform
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.mlab as mlab

# Read Image
if platform.system()=="Windows":
    im = mpimg.imread(r'..\..\Data\harris.png')
elif platform.system()=="Linux":
    im = mpimg.imread('../../Data/harris.png')
m, n, C = np.shape(im)
# Convert to grayscale if Image is RGB-channel
if C >= 3:
    r, g, b = im[:,:,0], im[:,:,1], im[:,:,2]
    im = 0.2126*r + 0.7152*g + 0.0722*b

# # Convolve Image with derivative filters.
# df = np.array([-1.0, 0.0, 1.0])
# Gx = scimg.filters.convolve1d(im, df, axis=1)
# Gy = scimg.filters.convolve1d(im, df, axis=0)
# Alternative filtering to original solution proposed by Harris
Gx = scimg.filters.gaussian_filter1d(im, 2.0, axis=1, order=1)
Gy = scimg.filters.gaussian_filter1d(im, 2.0, axis=0, order=1)

# Outer products of Gradients
Lx2 = scimg.filters.gaussian_filter1d(Gx**2, 3.0, order=0)   # Labeled A
Ly2 = scimg.filters.gaussian_filter1d(Gy**2, 3.0, order=0)   # Labeled B
Lxy = scimg.filters.gaussian_filter1d(Gx*Gy, 3.0, order=0)   # Labeled C

# Compute the Image Structure Tensor Matrix (Second Moment Matrix, Auto-Correlation Matrix)
alpha = 0.05
t = 0.01
E, R = np.zeros((m,n)), np.zeros((m,n))
for y in range(m):
    for x in range(n):
        M = np.array([[Lx2[y,x], Lxy[y,x]], [Lxy[y,x], Ly2[y,x]]])
        R[y,x] = np.linalg.det(M) - alpha*np.trace(M)**2
        E[y,x] = R[y,x]     # This is useless. Only to show thresholding
        if R[y,x]<t:
            R[y,x] = 0.0


# The histogram of the "Cornerness"
n, bins, patches = plt.hist(E.flatten(), 255, normed=1, facecolor='green', alpha=0.75)
plt.axis([np.min(E), np.max(E), 0, np.max(n)*1.05])
plt.grid(True)
plt.show()


# # Plot the "Cornerness" as a 3D surface
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = np.arange(n)
# Y = np.arange(m)
# X, Y = np.meshgrid(X, Y)
# surf = ax.plot_surface(X, Y, E, rstride=1, cstride=1, cmap=cm.coolwarm,
#         linewidth=0, antialiased=False)
# plt.show()


"""
Non-maxima Supression.
Based on Stackoverflow solution:
http://stackoverflow.com/questions/3684484/peak-detection-in-a-2d-array
"""
area  = scimg.morphology.generate_binary_structure(2,2)
lmax  = scimg.filters.maximum_filter(R, footprint=area)==R
bg    = (R==0)
e_bg  = scimg.morphology.binary_erosion(bg, structure=area, border_value=1)
spots = lmax - e_bg
peaks = np.nonzero(spots)  # Array with coordinates of Points


# Show images in grayscale
plt.subplot(2,3,1)
implot = plt.imshow(im, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(2,3,2)
Gx_plot = plt.imshow(Gx, cmap='gray')
plt.title('Gradient along X-axis')
plt.axis('off')
plt.subplot(2,3,3)
Gy_plot = plt.imshow(Gy, cmap='gray')
plt.title('Gradient along Y-axis')
plt.axis('off')
plt.subplot(2,3,4)
E_plot = plt.imshow(E, cmap='gray')
plt.colorbar(E_plot)
plt.title('Response (Cornerness)')
plt.axis('off')
plt.subplot(2,3,5)
R_plot = plt.imshow(R, cmap='gray')
plt.colorbar(R_plot)
plt.title('Thresholded result')
plt.axis('off')
plt.subplot(2,3,6)
implot = plt.imshow(im, cmap='gray')
p_plot = plt.plot(peaks[1], peaks[0], 'rx')
plt.title('Detected Points')
plt.axis('off')
plt.show()
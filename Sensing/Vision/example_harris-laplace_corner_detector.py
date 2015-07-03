# -*- coding: utf-8 -*-
"""
Breakdown of the Harris Corner detector.

This code plots each step estimating the corners in an image using the
"Harris Corner Detector" Algorithm.

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
    [5] Mikolajczyk, K. and Schmid, C. An affine invariant interest point
        detector. European Conference on Computer Vision (ECCV '02). 2002.

History:
    26.06.2015. First Implementation.
    28.06.2015. Added Sub-Plot.
    03.07.2015. Structure Tensor built.
                Simplified algorithm.
                Added References, and coding settings.

@author: Mario Garcia
www.mayitzin.com
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.ndimage as scimg
import numpy as np

# Read Image
im = mpimg.imread(r'..\..\Data\figures.png')	# On Windows
M, N, C = np.shape(im)
# Convert to grayscale if Image is RGB-channel
if C >= 3:
    r, g, b = im[:,:,0], im[:,:,1], im[:,:,2]
    im = 0.2989*r + 0.5870*g + 0.1140*b

# # Initial Parameters
# s0 = 1.5
# k = 1.2
# n = 0
# s_I = s0*k**n
# s_D = 0.7*s_I
# print "s_I is", s_I,"\ns_D is", s_D
mask = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])

Lx = scimg.filters.convolve1d(im, mask, axis=1)
Ly = scimg.filters.convolve1d(im, mask, axis=0)

# # Gradients: Convolution of Image with derivatives of Gaussians (order=1)
# Lx = scimg.filters.gaussian_filter1d(im, s_D, axis=1, order=1)
# Ly = scimg.filters.gaussian_filter1d(im, s_D, axis=0, order=1)

# Outer products of Gradients with Gaussian of sigma_I
# Lx2 = scimg.filters.gaussian_filter1d(Lx**2, s_I, order=0)
# Ly2 = scimg.filters.gaussian_filter1d(Ly**2, s_I, order=0)
# Lxy = scimg.filters.gaussian_filter1d(Lx*Ly, s_I, order=0)
Lx2 = scimg.filters.gaussian_filter1d(Lx**2, 1.0, order=0)
Ly2 = scimg.filters.gaussian_filter1d(Ly**2, 1.0, order=0)
Lxy = scimg.filters.gaussian_filter1d(Lx*Ly, 1.0, order=0)

# Compute the Image Structure Tensor Matrix (Second Moment Matrix, Auto-Correlation Matrix)
alpha = 0.06
t = 0.0
R = np.zeros((M,N))
for y in range(M):
	for x in range(N):
		# S = s_D*np.array([[Lx2[y,x], Lxy[y,x]], [Lxy[y,x], Ly2[y,x]]])
		S = np.array([[Lx2[y,x], Lxy[y,x]], [Lxy[y,x], Ly2[y,x]]])
		R[y,x] = np.linalg.det(S) - alpha*np.trace(S)**2
		# if R[y,x]<t:
		# 	R[y,x] = 0.0

# Show images in grayscale
plt.subplot(2,2,1)
implot = plt.imshow(im, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(2,2,2)
Lx_plot = plt.imshow(Lx, cmap='gray')
plt.title('Filtered X-axis')
plt.axis('off')
plt.subplot(2,2,3)
Ly_plot = plt.imshow(Ly, cmap='gray')
plt.title('Filtered Y-axis')
plt.axis('off')
plt.subplot(2,2,4)
R_plot = plt.imshow(R, cmap='gray')
plt.colorbar(R_plot)
plt.title('Structure Tensor')
plt.axis('off')


plt.show()
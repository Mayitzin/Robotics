"""
Breakdown of the Harris Corner detector

@author: Mario Garcia
www.mayitzin.com
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.ndimage as scimg
import numpy as np

# Read Image
im = mpimg.imread(r'..\..\Data\harris.png')
M, N, C = np.shape(im)
print "Y is", M, "\nX is", N
# Convert to grayscale if Image is RGB-channel
if C >= 3:
    r, g, b = im[:,:,0], im[:,:,1], im[:,:,2]
    im = 0.2989*r + 0.5870*g + 0.1140*b

# Convolution of Image with derivatives of Gaussians (Laplacians)
Lx = scimg.filters.gaussian_filter1d(im, 1, axis=1, order=1)
Ly = scimg.filters.gaussian_filter1d(im, 1, axis=0, order=1)

# Elements of Structure Tensor Matrix
Lx2 = Lx**2
Ly2 = Ly**2
Lxy = Lx*Ly

# Compute the Structure Tensor Matrix
alpha = 0.15
# t = -0.0035
R = np.zeros((M,N))
for y in range(M):
	for x in range(N):
		S = np.array([[Lx2[y,x], Lxy[y,x]], [Lxy[y,x], Ly2[y,x]]])
		R[y,x] = np.linalg.det(S) - alpha*np.trace(S)**2
		# if R[y,x]>t:
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
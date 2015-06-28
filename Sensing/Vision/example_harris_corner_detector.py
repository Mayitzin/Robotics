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
# Convert to grayscale if Image is RGB
if np.shape(im)[2] >= 3:
    r, g, b = im[:,:,0], im[:,:,1], im[:,:,2]
    im = 0.2989*r + 0.5870*g + 0.1140*b

fim = scimg.filters.gaussian_filter(im, 3, order=1)

# Show images in grayscale
plt.subplot(1,2,1)
implot = plt.imshow(im, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1,2,2)
fimplot = plt.imshow(fim, cmap='gray')
plt.title('Filtered Image')
plt.axis('off')


plt.show()
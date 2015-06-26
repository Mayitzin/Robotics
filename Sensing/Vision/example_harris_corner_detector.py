"""
Breakdown of the Harris Corner detector

@author: Mario Garcia
www.mayitzin.com
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Read Image
im = mpimg.imread(r'..\..\Data\atlante.jpg')

# Convert to grayscale if Image is RGB
if np.shape(im)[2] >= 3:
    r, g, b = im[:,:,0], im[:,:,1], im[:,:,2]
    im = 0.2989*r + 0.5870*g + 0.1140*b

# Show image in grayscale
implot = plt.imshow(im, cmap='gray')

plt.show()
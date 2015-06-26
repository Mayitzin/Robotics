"""
Breakdown of the Harris Corner detector

@author: Mario Garcia
www.mayitzin.com
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

im = mpimg.imread('..\..\Data\harris.png')
implot = plt.imshow(im)

plt.show()
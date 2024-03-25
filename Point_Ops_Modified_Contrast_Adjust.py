#a Python program to implement modified contrast
#adjustment method for point operations and comparing different percentage values.

import cv2
import matplotlib.pyplot as plt
import numpy as np

def adjustContrast(path, slow, shigh, output):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    
    #map low and up percental
    low = np.percentile(img, slow)
    up = np.percentile(img, shigh)

    #get rid of tails
    img = np.clip(img, low, up)

    #scale intensities
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite(output, img)

    return img

def plotHistogram(img, title):
    pixels = img.flatten()

    plt.hist(pixels, bins=256, range=(0,256), color='gray')
    plt.title(title)
    plt.show()

path='cameraman.jpg'
slow=3
shigh=97
output="adjustedCameramanPercentile3.jpg"
newImage=adjustContrast(path, slow, shigh, output)

img=cv2.imread(path, cv2.IMREAD_GRAYSCALE)

plotHistogram(img, 'Original Image Histogram')
plotHistogram(newImage, 'Adjusted Image Histogram')

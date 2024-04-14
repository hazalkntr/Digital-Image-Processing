import cv2
import numpy as np

original_image = cv2.imread('cameraman.jpg')

kernel_size = 11
kernel_motion_blur = np.zeros((kernel_size, kernel_size))
kernel_motion_blur[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
kernel_motion_blur = kernel_motion_blur / kernel_size

motion_blurred_image = cv2.filter2D(original_image, -1, kernel_motion_blur)

cv2.imshow('Original Image', original_image)
cv2.imshow('motion blurred Image', motion_blurred_image)
cv2.imwrite('motion_blurred_image.png', motion_blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
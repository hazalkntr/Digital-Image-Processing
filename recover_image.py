import cv2
import numpy as np

#load the image in grayscale mode
motion_blurred_image = cv2.imread('motion_blurred_image.png', cv2.IMREAD_GRAYSCALE)

if motion_blurred_image is None:
    print("Error: Could not load the motion blurred image.")
else:
    #define, create and normalize the motion blur kernel
    kernel_size = 11
    kernel_motion_blur = np.zeros((kernel_size, kernel_size))
    kernel_motion_blur[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
    kernel_motion_blur = kernel_motion_blur / kernel_size

    #Fourier transform of the motion blur kernel
    f_kernel_motion_blur = np.fft.fft2(kernel_motion_blur, s=motion_blurred_image.shape)

    #Fourier transform of the motion blurred image
    f_motion_blurred = np.fft.fft2(motion_blurred_image)

    #noise parameter for wiener filtering , and then compute it
    noise_variance = 0.0009
    wiener_filter = np.conj(f_kernel_motion_blur) / (np.abs(f_kernel_motion_blur)**2 + noise_variance)

    #wiener deconvolution
    f_deblurred = wiener_filter * f_motion_blurred
    
    #inverse Fourier transform
    deblurred_image = np.fft.ifft2(f_deblurred).real

    cv2.imshow('Motion Blurred Image', motion_blurred_image.astype(np.uint8))
    cv2.imshow('Deblurred Image', deblurred_image.astype(np.uint8))
    cv2.imwrite('deblurred_image.png', deblurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
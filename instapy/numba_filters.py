"""numba-optimized filters"""
from numba import jit
import numpy as np


@jit(nopython=True)
def numba_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image) 
    # Iterating through the pixels, applying the grayscale transform
    H,W,C = image.shape
    for i in range(H): # For each row:
        for j in range(W): # For each value in the row:
            # Calculating grayscale transform
            grayscale_transform =0.21*image[i,j,0] + 0.72*image[i,j,1] + 0.07*image[i,j,2] 
            gray_image[i, j, 0] = grayscale_transform # Applying to R channel
            gray_image[i, j, 1] = grayscale_transform # Applying to G channel
            gray_image[i, j, 2] = grayscale_transform # Applying to B channel

    gray_image = gray_image.astype("uint8") # Converting pixel values back to uint8

    return gray_image


@jit(nopython=True)
def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)

    sepia_matrix = np.array([
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ])

    # Iterating through the pixels, applying the sepia matrix
    H,W,C = image.shape
    for i in range(H): # For each row:
        for j in range(W): # For each value in the row:
            # Calculate and apply sepia values for each color channel
            sepia_image[i, j, 0] = min(image[i,j,0]*sepia_matrix[0,0] + image[i,j,1]*sepia_matrix[0,1] + image[i,j,2]*sepia_matrix[0,2], 255)
            sepia_image[i, j, 1] = min(image[i,j,0]*sepia_matrix[1,0] + image[i,j,1]*sepia_matrix[1,1] + image[i,j,2]*sepia_matrix[1,2], 255)
            sepia_image[i, j, 2] = min(image[i,j,0]*sepia_matrix[2,0] + image[i,j,1]*sepia_matrix[2,1] + image[i,j,2]*sepia_matrix[2,2], 255)

    sepia_image = sepia_image.astype("uint8") # Converting pixel values back to uint8

    return sepia_image
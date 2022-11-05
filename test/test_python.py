from instapy.python_filters import python_color2gray, python_color2sepia

import numpy as np

def test_color2gray(image):
    # run color2gray
    gray_image = python_color2gray(image)

    # check that the result has the right shape, type
    assert isinstance(gray_image, np.ndarray)
    assert gray_image.shape == image.shape
    # assert uniform r,g,b values
    assert gray_image[0, 0, 0] == gray_image[0, 0, 1]
    assert gray_image[0, 0, 1] == gray_image[0, 0, 2] 



def test_color2sepia(image):
    # run color2sepia
    sepia_image = python_color2sepia(image)

    # check that the result has the right shape, type
    assert isinstance(sepia_image, np.ndarray)
    assert sepia_image.shape == image.shape
    
    # verify some individual pixel samples
    # according to the sepia matrix
    sepia_matrix = np.array([
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ])
    assert sepia_image[0,0,0] == int(min(image[0,0,0]*sepia_matrix[0,0] + image[0,0,1]*sepia_matrix[0,1] + image[0,0,2]*sepia_matrix[0,2], 255))
    assert sepia_image[10,10,1] == int(min(image[10,10,0]*sepia_matrix[1,0] + image[10,10,1]*sepia_matrix[1,1] + image[10,10,2]*sepia_matrix[1,2], 255))
    assert sepia_image[100,100,2] == int(min(image[100,100,0]*sepia_matrix[2,0] + image[100,100,1]*sepia_matrix[2,1] + image[100,100,2]*sepia_matrix[2,2], 255))

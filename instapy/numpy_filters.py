"""numpy implementation of image filters"""

from typing import Optional
import numpy as np


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_image =  np.empty_like(image)

    # Using numpy slicing in order to have fast vectorized code
    gray = 0.21*image[:,:,0] + 0.72*image[:,:,1] + 0.07*image[:,:,2] # Gray is now a 2D array
    # Stacking together the 2D arrays in all color channels, giving all channels the same values
    gray_image = np.dstack((gray,gray,gray)) # gray_image is now a 3D array

    gray_image = gray_image.astype("uint8") # Converting pixel values back to uint8

    return gray_image


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # Validating k
        raise ValueError(f"k must be between [0-1], got {k=}")

    sepia_image = np.empty_like(image)

    # Defining sepia matrix with `k` tuning parameter
    sepia_matrix = np.array([
        [ 1 - k * (1 - 0.393), k * 0.769, k * 0.189],
        [ k * 0.349, 1 - k * (1 - 0.686), k * 0.168],
        [ k * 0.272, k * 0.534, 1 - k * (1 - 0.131)],
    ])

    # Using Einstein sum to apply the pixel transform matrix
    sepia_image = np.einsum("ijk, lk -> ijl", image, sepia_matrix)

    # Checking which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    sepia_image[sepia_image > 255] = 255

    # Return image (make sure it's the right type!)
    sepia_image = sepia_image.astype("uint8") # Converting pixel values back to uint8

    return sepia_image

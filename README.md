# instapy

instapy is a Python package for adding gray or sepia filters to an image.

## Installation

With the instapy package downloaded, use the package manager [pip](https://pip.pypa.io/en/stable/) to install instapy. 
From a terminal, enter the directory holding the instapy project, and enter the following:

```bash
python3 -m pip install .
```

## Usage

The following are usage instructions from different contexts.

### From a terminal

In the terminal, input commands on the following format to add filters to a given image:

```bash
instapy [-h] [-o OUT] [-g | -se] [-sc SCALE] [-i {python,numba,numpy}] [-r] file
```
or the following:
```bash
python3 -m instapy [-h] [-o OUT] [-g | -se] [-sc SCALE] [-i {python,numba,numpy}] [-r] file
```

The passable arguments are explained here:

```bash
positional arguments:
  file                  The filename to apply filter to

options:
  -h, --help            show this help message and exit
  -o OUT, --out OUT     The output filename
  -g, --gray            Select gray filter
  -se, --sepia          Select sepia filter
  -sc SCALE, --scale SCALE
                        Scale factor to resize image
  -i {python,numba,numpy}, --implementation {python,numba,numpy}
                        The implementation
  -r, --runtime         Track average runtime
```

### When programming in Python

In Python, convert an image to a numpy array, then call the following functions to add filters to the image using the implementations given in the names:

```python
import instapy

# returns the grayed image as a numpy array
instapy.python_color2gray(image_as_nparray)

# returns the sepia filtered image as a numpy array
instapy.python_color2sepia(image_as_nparray)

# returns the grayed image as a numpy array, using numpy vectorization in the implementation
instapy.numpy_color2gray(image_as_nparray)

# returns the sepia filtered image as a numpy array, using numpy vectorization in the implementation
instapy.numpy_color2sepia(image_as_nparray)

# returns the grayed image as a numpy array, using the jit decorator from numba in the implementation
instapy.numba_color2gray(image_as_nparray)

# returns the sepia filtered image as a numpy array, using the jit decorator from numba in the implementation
instapy.numba_color2sepia(image_as_nparray)
```

More information is provided within the docstrings of the functions.
"""Command-line (script) interface to instapy"""

import argparse
import sys
import time

import numpy as np
from PIL import Image

import instapy
from . import get_filter, io


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1, 
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = Image.open(file)
    if scale != 1:
        # Resize image, if needed
        image = image.resize((int(image.width * scale), int(image.height * scale)))
    image = np.asarray(image)

    # Apply the filter
    filter_function = get_filter(filter, implementation)
    filtered = filter_function(image)
    if out_file:
        # save the file
        io.write_image(filtered, out_file)
    else:
        # not asked to save, display it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    # Add required arguments
    group.add_argument("-g", "--gray", help="Select gray filter", action='store_true')
    group.add_argument("-se", "--sepia", help="Select sepia filter", action='store_true')
    parser.add_argument("-sc", "--scale", help="Scale factor to resize image", type=float)
    parser.add_argument("-i", "--implementation", help="The implementation", choices={"python","numba","numpy"})
    parser.add_argument("-r", "--runtime", help="Track average runtime", action='store_true')

    # parse arguments and call run_filter
    namespace = parser.parse_args()

    filter_vars = [] #Adding input arguments to list
    filter_vars.append(namespace.file)
    filter_vars.append(namespace.out) if namespace.out is not None else filter_vars.append(None)
    filter_vars.append(namespace.implementation) if namespace.implementation is not None else filter_vars.append("python")
    if namespace.sepia: filter_vars.append("color2sepia")
    else: filter_vars.append("color2gray")
    filter_vars.append(namespace.scale) if namespace.scale is not None else filter_vars.append(1)

    if not namespace.runtime: run_filter(*filter_vars)
    else:
        start_time = time.time()
        avg_time = 0
        for _ in range(3):
            run_filter(*filter_vars)
            run_time = time.time() - start_time
            avg_time += run_time
            start_time = time.time()
        avg_time = avg_time / 3
        print(f"Average time over 3 runs: {round(avg_time, 3)}s")
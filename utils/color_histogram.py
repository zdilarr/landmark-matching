"""
    Helper method for calculating histogram of R/G/B intensity.
    Author: Emilija Zdilar 23-02-2019.
"""

import numpy as np

from utils.hog import nearest_index


def histogram_of_image_color(img: np.ndarray, hist_bins: np.array, bin_difference_half: float) -> np.array:
    """
    Method that calculates histogram of an entire image represented by numpy array.
    Args:
        img: Input image
        hist_bins: Array that splits intensities 0-255 into bins
        bin_difference_half: median between two elements of the array hist_bins

    Returns: numpy array that represents the histogram of image

    """

    img_hist = np.zeros(shape=hist_bins.size)
    img_size_1 = img.shape[0]
    img_size_2 = img.shape[1]

    for row_idx in range(img_size_1):
        for col_idx in range(img_size_2):
            curr_intensity = img[row_idx, col_idx]
            hist_bin_index_list = nearest_index(hist_bins, curr_intensity, bin_difference_half)
            for index in hist_bin_index_list:
                img_hist[index] += curr_intensity / len(hist_bin_index_list)
    return img_hist

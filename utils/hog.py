"""
    Helper methods for calculating histogram of oriented gradients.
    Author: Emilija Zdilar 13-02-2019
"""

import numpy as np

from utils.constants import EPS, BIN_DIFFERENCE_HALF, HORIZONTAL_MASK, VERTICAL_MASK, HIST_BINS


def calculate_gradient(img: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """
    Method that takes greyscale image and calculates the gradient, horizontal or vertical.
    Used for HOG, edge detection, etc.
    Args:
        img: input image as numpy array
        mask: horizontal or vertical gradient mask (in constants.py)

    Returns: gradient image.
    """

    padding = mask.size
    first_image_pixel = np.uint16((padding-1)/2.0)
    no_of_rows = img.shape[0]
    no_of_columns = img.shape[1]

    new_img = np.full((no_of_rows+padding-1, no_of_columns+padding-1), int(np.mean(img)))
    new_img[first_image_pixel:no_of_rows+first_image_pixel, first_image_pixel:no_of_columns+first_image_pixel] = img
    result = np.zeros(new_img.shape)

    for row in np.arange(first_image_pixel, no_of_rows+first_image_pixel):
        for column in np.arange(first_image_pixel, no_of_columns+first_image_pixel):
            curr_region = new_img[row - first_image_pixel: row+first_image_pixel+1,
                                  column-first_image_pixel:column+first_image_pixel+1]
            curr_result = curr_region * mask
            score = np.sum(curr_result)
            result[row, column] = score

    result_img = result[first_image_pixel:result.shape[0]-first_image_pixel,
                        first_image_pixel:result.shape[1]-first_image_pixel]
    return result_img


def gradient_magnitudes(horizontal_gradient: np.ndarray, vertical_gradient: np.ndarray) -> np.ndarray:
    """
    Method that calculates gradient magnitudes.
    Args:
        horizontal_gradient: horizontal gradient of an input image
        vertical_gradient: vertical gradient of an input image

    Returns: array of magnitudes
    """
    return np.sqrt(np.power(horizontal_gradient, 2) + np.power(vertical_gradient, 2))


def gradient_directions(horizontal_gradient: np.ndarray, vertical_gradient: np.ndarray) -> np.ndarray:
    """
    Method that calculates gradient directions.
    Args:
        horizontal_gradient:  horizontal gradient of an input image
        vertical_gradient: vertical gradient of an input image

    Returns: array of directions

    """
    grad_direction = np.rad2deg(np.arctan(vertical_gradient/(horizontal_gradient + EPS)))
    return grad_direction % 180


def nearest_index(array: np.ndarray, value: float, bin_difference_half: float) -> np.ndarray:
    """
    Method that calculates index of the closest element
    Args:
        bin_difference_half: median between two elements of the array
        array: array of values
        value: given value

    Returns: index of the element whose value is the closest to a given one.
    """

    array = np.asarray(array)
    index = (np.abs(array - value)).argmin()
    result = np.array([index])
    if value - array[index] == bin_difference_half:
        result = np.array([index, (index+1) % array.size])
    return result


def histogram_of_oriented_gradients_cell(cell_gradient_directions: np.ndarray,
                                         cell_gradient_magnitudes: np.ndarray, hist_bins: np.array) -> np.array:
    """
    Method that calculates histogram of oriented gradients for a defined window cell area.
    Args:
        cell_gradient_directions: calculated gradient directions for pixels inside cells
        cell_gradient_magnitudes: calculated gradients for pixels inside cells
        hist_bins: array that splits angles 0 - 180 into bins

    Returns: hog

    """

    cell_hog = np.zeros(shape=hist_bins.size)
    cell_size_1 = cell_gradient_directions.shape[0]
    cell_size_2 = cell_gradient_directions.shape[1]

    for row_idx in range(cell_size_1):
        for col_idx in range(cell_size_2):
            curr_direction = cell_gradient_directions[row_idx, col_idx]
            curr_magnitude = cell_gradient_magnitudes[row_idx, col_idx]
            hist_bin_index_list = nearest_index(hist_bins, curr_direction, BIN_DIFFERENCE_HALF)
            for index in hist_bin_index_list:
                cell_hog[index] += curr_magnitude / len(hist_bin_index_list)
    return cell_hog


def hog_of_image(img: np.ndarray) -> np.array:
    """
    Method that calculates histogram of an entire image, with the help
    of the histogram_of_oriented_gradients_cell method.

    Args:
        img: image represented by numpy array

    Returns: array that represents histogram of oriented gradients

    """
    horizontal_gradient = calculate_gradient(img, HORIZONTAL_MASK)
    vertical_gradient = calculate_gradient(img, VERTICAL_MASK)

    grad_magnitude = gradient_magnitudes(horizontal_gradient, vertical_gradient)
    grad_direction = gradient_directions(horizontal_gradient, vertical_gradient)

    return histogram_of_oriented_gradients_cell(grad_direction, grad_magnitude, HIST_BINS)


def sum_all_magnitudes(img: np.ndarray) -> int:
    """
    Helper method that sums all magnitudes of gradients in an image,
    used for calculating maximum difference between two images based
    on the hog criteria. Maximum difference is needed to determine a
    percentage of similarity between two images.

    Args:
        img: image represented by numpy array.

    Returns: closest integer to sum of all gradients

    """
    horizontal_gradient = calculate_gradient(img, HORIZONTAL_MASK)
    vertical_gradient = calculate_gradient(img, VERTICAL_MASK)

    grad_magnitude = gradient_magnitudes(horizontal_gradient, vertical_gradient)
    return int(np.sum(grad_magnitude))

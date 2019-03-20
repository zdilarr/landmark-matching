"""
    Util file wrapper for reading image and calculating similarities.
    Author: Emilija Zdilar 23-02-2019
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

from utils.color_histogram import histogram_of_image_color
from utils.constants import BIN_DIFFERENCE_INTENSITY_HALF, HIST_BINS_INTENSITY, RGB_COMPONENTS, THRESHOLD, SAME_LANDMARK
from utils.hog import hog_of_image, sum_all_magnitudes


def read_image_greyscale(path: str) -> np.ndarray:
    """
    Helper method that reads and, if necessary,
    converts input image to greyscale.
    Args:
        path: path to image

    Returns: image as numpy array

    """
    img = imread(path)
    if len(img.shape) > 2:
        img = np.dot(img[..., :3], [0.299, 0.587, 0.114])
    return img


def read_image_color(path: str, color: str) -> np.ndarray:
    """
    Helper method that reads and extracts color component from
    an image. RGB color space is implied.

    Args:
        path: path to image file
        color: color component - red, green or blue.

    Returns: image as numpy array

    """
    img = imread(path)
    if color == 'red':
        return img[:, :, 0]
    elif color == 'green':
        return img[:, :, 1]
    elif color == 'blue':
        return img[:, :, 2]
    return read_image_greyscale(path)


def similarity_two_images_hog(img1: np.ndarray, img2: np.ndarray) -> np.ndarray:
    """
    Method that calculates percentage of similarity between the two images,
    based on the histogram of oriented gradients criteria.
    Args:
        img1: input image
        img2: input image

    Returns: Number between 0 and 100. The bigger the number, the higher the chance
    that the two images represent the same landmark.

    """
    hog_image1 = hog_of_image(img1)
    hog_image2 = hog_of_image(img2)

    max_difference = max(2 * sum_all_magnitudes(img1), 2 * sum_all_magnitudes(img2))
    return 100 - 100 * np.sum(np.absolute(hog_image1 - hog_image2)) / max_difference


def similarity_two_images_color(img1: np.ndarray, img2: np.ndarray) -> np.ndarray:
    """
    Method that calculates percentage of similarity between the two images,
    based on the color intensity histogram .
    Args:
        img1: input image
        img2: input image

    Returns: Number between 0 and 100. The bigger the number, the higher the chance
    that the two images represent the same landmark.

    """
    hist_image_1 = histogram_of_image_color(img1, HIST_BINS_INTENSITY, BIN_DIFFERENCE_INTENSITY_HALF)
    hist_image_2 = histogram_of_image_color(img2, HIST_BINS_INTENSITY, BIN_DIFFERENCE_INTENSITY_HALF)
    max_difference = max(2 * np.sum(hist_image_1), 2 * np.sum(hist_image_2))
    return 100 - 100 * np.sum(np.absolute(hist_image_1 - hist_image_2)) / max_difference


def same_landmark_images(path_1: str, path_2: str) -> float:
    """
    Method that calculates certainty that two images represent the same image.
    Similarity is calculated based on the HOG, R, G, B gradients, and the
    weighted average of the degree of similarity is returned.
    Args:
        path_1: path to input image
        path_2: path to input image

    Returns: Number between 0 and 100. The bigger the number, the higher the chance
    that the two images represent the same landmark.

    """
    img_1_greyscale = read_image_greyscale(path_1)
    img_2_greyscale = read_image_greyscale(path_2)
    img_1_rgb_separated = np.array([read_image_color(path_1, component) for component in RGB_COMPONENTS])
    img_2_rgb_separated = np.array([read_image_color(path_2, component) for component in RGB_COMPONENTS])

    similarity_hog = similarity_two_images_hog(img_1_greyscale, img_2_greyscale)
    similiarities_rgb = np.array([similarity_two_images_color(img_1_rgb_separated[i], img_2_rgb_separated[i])
                                  for i in range(0, len(RGB_COMPONENTS))])
    similarity_color = np.mean(similiarities_rgb)

    similarity_percentage = np.average([similarity_hog, similarity_color], weights=[1.2, 1])
    return float(similarity_percentage)


def visualize_results_same_landmark(img_1: str, img_2: str) -> None:
    """
    Method that visualizes input images and returns the YES/NO answer.
    If the result from same_landmark_images is above the threshold, the
    answer will be YES. Otherwise, answer will be NO.
    Args:
        img_1: path to input image
        img_2: path to input image

    Returns: None.

    """

    similarity_percentage = same_landmark_images(img_1, img_2)
    print(similarity_percentage)
    same_landmark = 'YES' if similarity_percentage > THRESHOLD else 'NO'

    fig = plt.figure()
    ax = fig.add_subplot(121)
    ax.imshow(imread(img_1))
    ax.set_title('')

    ax = fig.add_subplot(122)
    ax.set_title('')
    ax.imshow(imread(img_2))

    fig.suptitle(SAME_LANDMARK + same_landmark, fontsize=16)
    fig.tight_layout()
    plt.show()

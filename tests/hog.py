import unittest
import numpy as np

from utils.constants import EPS, BIN_DIFFERENCE_HALF
from utils.hog import gradient_magnitudes, gradient_directions, nearest_index


class TestHogGradientMethods(unittest.TestCase):

    def setUp(self):
        self.horizontal_gradient = np.array([50, 60])
        self.vertical_gradient = np.array([50, 30])

    def test_gradient_magnitudes(self):
        magnitudes = gradient_magnitudes(self.horizontal_gradient, self.vertical_gradient)
        result = np.array([70.71, 67.08])
        self.assertAlmostEqual(magnitudes[0], result[0], places=2)
        self.assertAlmostEqual(magnitudes[1], result[1], places=2)

    def test_gradient_directions(self):
        directions = gradient_directions(self.horizontal_gradient, self.vertical_gradient)
        result = np.rad2deg(np.arctan(self.vertical_gradient / (self.horizontal_gradient + EPS))) % 180
        self.assertAlmostEqual(directions[0], result[0], places=2)
        self.assertAlmostEqual(directions[1], result[1], places=2)

    def tearDown(self):
        pass


class TestHogNearestIndex(unittest.TestCase):

    def setUp(self):
        self.array = np.array([20, 40, 60, 80])
        self.value_1 = 22
        self.value_middle = 50

    def test_closest_element(self):
        nearest_idx = np.array([0])
        self.assertSequenceEqual(list(nearest_idx), list(nearest_index(self.array, self.value_1, BIN_DIFFERENCE_HALF,)))

    def test_middle_element(self):
        nearest_idx = np.array([1, 2])
        self.assertSequenceEqual(list(nearest_idx),
                                 list(nearest_index(self.array, self.value_middle, BIN_DIFFERENCE_HALF,)))

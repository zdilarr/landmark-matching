"""
    Histogram of oriented gradients for the Lena image.
    Author: Emilija Zdilar 15-02-2019
"""

import matplotlib.pyplot as plt
from matplotlib import patches
from utils.constants import TEST_IMAGES_PATH, TEST_LENNA, HORIZONTAL_MASK, VERTICAL_MASK, START, END, HIST_BINS, \
    MAGNITUDE_LABEL, ORIENTATION_LABEL, GRAY, BAR_WIDTH, LINE_WIDTH, GREEN, INPUT_IMAGE_SUBTITLE, HOG_SUBTITLE, \
    HORIZONTAL_GRADIENT_SUBTITLE, VERTICAL_GRADIENT_SUBTITLE, NEAREST_INTERPOLATION, CENTER
from utils import image, hog

img = image.read_image_greyscale(TEST_IMAGES_PATH+TEST_LENNA)

horizontal_gradient = hog.calculate_gradient(img, HORIZONTAL_MASK)
vertical_gradient = hog.calculate_gradient(img, VERTICAL_MASK)

grad_magnitude = hog.gradient_magnitudes(horizontal_gradient, vertical_gradient)
grad_direction = hog.gradient_directions(horizontal_gradient, vertical_gradient)

cell_gradient_directions = grad_direction[START:END, START:END]
cell_gradient_magnitudes = grad_magnitude[START:END, START:END]


HOG_cell_hist = hog.histogram_of_oriented_gradients_cell(cell_gradient_directions, cell_gradient_magnitudes, HIST_BINS)

fig = plt.figure()
ax = fig.add_subplot(221)
ax.imshow(img, interpolation=NEAREST_INTERPOLATION, cmap=GRAY)
ax.add_patch(patches.Rectangle((START, START), 50, 50, color=GREEN, linewidth=LINE_WIDTH, fill=False))
ax.set_title(INPUT_IMAGE_SUBTITLE)

plt.subplot(222).set_title(HOG_SUBTITLE)
plt.bar(x=HIST_BINS, height=HOG_cell_hist, align=CENTER, width=BAR_WIDTH, color=GRAY)
plt.xticks(HIST_BINS)
plt.ylabel(MAGNITUDE_LABEL)
plt.xlabel(ORIENTATION_LABEL)
plt.yticks([])

ax = fig.add_subplot(223)
ax.set_title(HORIZONTAL_GRADIENT_SUBTITLE)
ax.imshow(horizontal_gradient, interpolation=NEAREST_INTERPOLATION, cmap=GRAY)
ax = fig.add_subplot(224)
ax.imshow(vertical_gradient, interpolation=NEAREST_INTERPOLATION, cmap=GRAY)
ax.set_title(VERTICAL_GRADIENT_SUBTITLE)
fig.tight_layout()
plt.show()

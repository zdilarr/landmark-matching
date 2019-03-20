import numpy as np

# Paths for test images
TEST_IMAGES_PATH = 'test_images/'
TEST_LENNA = 'test_lenna.png'
TEST_CATHEDRAL_1 = 'test_cathedral_1.jpg'
TEST_CATHEDRAL_2 = 'test_cathedral_2.jpg'
TEST_CATHEDRAL_3 = 'test_cathedral_3.jpg'
TEST_SKY = 'test_sky.jpg'
TEST_BRICK = 'test_brick.jpg'
TEST_TAJ_MAHAL_1 = 'taj_mahal_1.png'
TEST_TAJ_MAHAL_2 = 'taj_mahal_2.png'
TEST_TAJ_MAHAL_rotated = 'taj_mahal_rotated.png'
TEST_DOM_1 = 'dom_1.png'
TEST_DOM_2 = 'dom_2.png'
TEST_SOL_1 = 'statue_of_liberty_1.jpg'
TEST_SOL_2 = 'statue_of_liberty_2.jpg'
TEST_SOL_3 = 'statue_of_liberty_3.jpg'
TEST_SOL_4 = 'statue_of_liberty_4.jpg'
TEST_BUILDING_DAY = 'building_day.png'
TEST_BUILDING_NIGHT = 'building_night.png'
TEST_SARAJEVO_CATHEDRAL_1 = 'sarajevo_cathedral_1.jpg'
TEST_SARAJEVO_CATHEDRAL_2 = 'sarajevo_cathedral_2.jpg'

# HOG
HORIZONTAL_MASK = np.array([-1, 0, 1])
VERTICAL_MASK = np.array([[-1], [0], [1]])
EPS = 0.00000001
HIST_BINS = np.array([10, 30, 50, 70, 90, 110, 130, 150, 170])
HIST_BINS_INTENSITY = np.array([32, 96, 160, 224])
BIN_DIFFERENCE_HALF = 10
BIN_DIFFERENCE_INTENSITY_HALF = 32
MAGNITUDE_LABEL = 'Magnitude'
ORIENTATION_LABEL = 'Orientation'
START = 100
END = 150
LINE_WIDTH = 3

# colors
GRAY = 'gray'
RED = 'red'
GREEN = 'green'
BLUE = 'blue'
RGB_COMPONENTS = [RED, GREEN, BLUE]


# Visualization
BAR_WIDTH = 15
INPUT_IMAGE_SUBTITLE = 'Input image'
VERTICAL_GRADIENT_SUBTITLE = 'Vertical gradient'
HORIZONTAL_GRADIENT_SUBTITLE = 'Horizontal gradient'
HOG_SUBTITLE = 'HOG'
NEAREST_INTERPOLATION = 'nearest'
CENTER = 'center'

SIMILARITY_PERCENTAGE = "Similarity percentage: "
SAME_LANDMARK = "Same landmark: "

# Similarity threshold
THRESHOLD = 75

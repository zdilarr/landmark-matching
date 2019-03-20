"""
    Algorithm that for two given images, returns the answer to the question if they contain the same landmark.
    Author: Emilija Zdilar 24-02-2019
"""

from utils.constants import TEST_IMAGES_PATH, TEST_CATHEDRAL_1, \
    TEST_CATHEDRAL_2, TEST_CATHEDRAL_3, TEST_LENNA, TEST_SKY, TEST_BRICK, TEST_TAJ_MAHAL_1, TEST_TAJ_MAHAL_rotated, \
    TEST_TAJ_MAHAL_2, TEST_DOM_1, TEST_DOM_2, TEST_SOL_1, TEST_SOL_2, TEST_BUILDING_NIGHT, TEST_BUILDING_DAY, \
    TEST_SOL_3, TEST_SOL_4, TEST_SARAJEVO_CATHEDRAL_2, TEST_SARAJEVO_CATHEDRAL_1
from utils.image import visualize_results_same_landmark

# loading paths
img_lenna = TEST_IMAGES_PATH + TEST_LENNA
img_sky = TEST_IMAGES_PATH + TEST_SKY
img_bricks = TEST_IMAGES_PATH + TEST_BRICK
img_cathedral_1 = TEST_IMAGES_PATH + TEST_CATHEDRAL_1
img_cathedral_2 = TEST_IMAGES_PATH + TEST_CATHEDRAL_2
img_cathedral_3 = TEST_IMAGES_PATH + TEST_CATHEDRAL_3
img_taj_mahal_1 = TEST_IMAGES_PATH + TEST_TAJ_MAHAL_1
img_taj_mahal_2 = TEST_IMAGES_PATH + TEST_TAJ_MAHAL_2
img_taj_mahal_rotated = TEST_IMAGES_PATH + TEST_TAJ_MAHAL_rotated
img_dom_1 = TEST_IMAGES_PATH + TEST_DOM_1
img_dom_2 = TEST_IMAGES_PATH + TEST_DOM_2
img_sol_1 = TEST_IMAGES_PATH + TEST_SOL_1
img_sol_2 = TEST_IMAGES_PATH + TEST_SOL_2
img_sol_3 = TEST_IMAGES_PATH + TEST_SOL_3
img_sol_4 = TEST_IMAGES_PATH + TEST_SOL_4
img_building_day = TEST_IMAGES_PATH + TEST_BUILDING_DAY
img_building_night = TEST_IMAGES_PATH + TEST_BUILDING_NIGHT
img_sarajevo_cathedral_1 = TEST_IMAGES_PATH + TEST_SARAJEVO_CATHEDRAL_1
img_sarajevo_cathedral_2 = TEST_IMAGES_PATH + TEST_SARAJEVO_CATHEDRAL_2

# algorithm visualization
visualize_results_same_landmark(img_dom_1, img_dom_2)
# visualize_results_same_landmark(img_sky, img_bricks)
# visualize_results_same_landmark(img_cathedral_1, img_cathedral_2)
# visualize_results_same_landmark(img_taj_mahal_1, img_taj_mahal_2)
# visualize_results_same_landmark(img_taj_mahal_1, img_taj_mahal_rotated)
# visualize_results_same_landmark(img_sol_1, img_sol_2)
# visualize_results_same_landmark(img_sol_1, img_dom_2)
# visualize_results_same_landmark(img_building_day, img_building_night)
# visualize_results_same_landmark(img_sol_1, img_sol_3)
# visualize_results_same_landmark(img_sol_1, img_sol_4)
# visualize_results_same_landmark(img_sarajevo_cathedral_1, img_sarajevo_cathedral_2)

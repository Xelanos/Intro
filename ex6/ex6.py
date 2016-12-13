import math

RED = 0
GREEN = 1
BLUE = 2


def compare_pixel(pixel1, pixel2):
    """
    A function that takes two pixels ( a tuple of RGB) and returns
    one number which stands for the total difference in color between
    the two pixels.
    """
    total_red = pixel1[RED] - pixel2[RED]
    total_green = pixel1[GREEN] - pixel2[GREEN]
    total_blue = pixel1[BLUE] - pixel2[BLUE]
    total_difference = math.fabs(total_red) + math.fabs(total_green) +\
                       math.fabs(total_blue)
    return total_difference


def compare(image1, image2):
    """
    :param image1, image2: a list of lists such as that the outer list
     indicate rows and the inner lists the columns (of pixels)
    :return: the sum of the distance between each pixel in each image which
    indicates a measurable comparison between them
    """
    total_distance = 0   # starting value
    max_rows = max(len(image1), len(image2))
    max_columns = max(len(image1[0]), len(image2[0]))
    for row in range(max_rows):
        for column in range(max_columns):
            pixel_distance = compare_pixel(image1[row][column],
                                           image2[row][column])
            total_distance += pixel_distance  # add each pixel to total
    return total_distance


def get_piece(image, upper_left, size):
    """
    A function which cropes the images to required size
    :param image: a list of lists such as that the outer list
     indicate rows and the inner lists the columns (of pixels)
    :param upper_left: tuple of 2 ints which indicates the starting position
    of the crop (top left corner)
    :param size: the size which we want to crop
    :return: the cropped image in the form of a list of lists
     such as that the outer list indicate rows
     and the inner lists the columns (of pixels)
    """
    max_rows_allowed = len(image)
    max_columns_allowed = len(image[0])
    final_height = upper_left[0] + size[0]
    final_width = upper_left[1] + size[1]
    if final_height <= max_rows_allowed:
        if final_width <= max_columns_allowed:
            cropped_image = [image[row][:final_width]
                             for row in range(final_height)]
        else:
            cropped_image = [image[row][:max_columns_allowed]
                             for row in range(final_height)]
    else:
        if final_width <= max_columns_allowed:
            cropped_image = [image[row][:final_width]
                             for row in range(max_rows_allowed)]
        else:
            cropped_image = [image[row][:max_columns_allowed]
                             for row in range(max_rows_allowed)]
    return cropped_image



def set_piece(image, upper_left, piece):
    pass


def average(image):
    pass


def preprocess_tiles(tiles):
    pass


def get_best_tiles(objective, tiles, averages, num_candidates):
    pass


def choose_tile(piece, tiles):
    pass


def make_mosaic(image, tiles, num_candidates):
    pass

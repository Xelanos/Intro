import math
import sys
import mosaic

RED = 0
GREEN = 1
BLUE = 2
HEIGHT = 0
WIDTH = 1
NUMBER_OF_ARGUMENTS = 5
WRONG_ARG = 'Wrong number of parameters. The correct usage is:\n' \
            'ex6.py <image_source> <images_dir> <output_name> ' \
            '<tile_height> <num_candidates>'


def compare_pixel(pixel1, pixel2):
    """
    A function that takes two pixels ( a tuple of RGB) and returns
    one number which stands for the total difference in color between
    the two pixels.
    """
    total_red = pixel1[RED] - pixel2[RED]
    total_green = pixel1[GREEN] - pixel2[GREEN]
    total_blue = pixel1[BLUE] - pixel2[BLUE]
    total_difference = math.fabs(total_red) + math.fabs(total_green) + \
                       math.fabs(total_blue)
    return total_difference


def compare(image1, image2):
    """
    :param image1, image2: a list of lists such as that the outer list
     indicate rows and the inner lists the columns (of pixels)
    :return: the sum of the distance between each pixel in each image which
    indicates a measurable comparison between them
    """
    total_distance = 0  # starting value
    max_rows = min(len(image1), len(image2))
    max_columns = min(len(image1[0]), len(image2[0]))
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
    # values
    max_rows_allowed = len(image)
    max_columns_allowed = len(image[0])
    expected_height = upper_left[HEIGHT] + size[HEIGHT]
    expected_width = upper_left[WIDTH] + size[WIDTH]
    # getting the final row/column allowed
    final_height = min(max_rows_allowed, expected_height)
    final_width = min(max_columns_allowed, expected_width)
    # the smart part
    cropped_image = []
    for row in range(upper_left[HEIGHT], final_height):
        row_list = image[row][upper_left[WIDTH]:final_width]
        cropped_image.append(row_list)
    return cropped_image


def set_piece(image, upper_left, piece):
    """
    A function that sets a new image in a section of the original image
    :param image: the original image (list of lists of pixels)
    :param upper_left: where to start the set of the new image
    :param piece: the new image (list of lists of pixels)
    """
    # values
    max_rows_allowed = len(image)
    max_columns_allowed = len(image[0])
    expected_height = upper_left[HEIGHT] + len(piece)
    expected_width = upper_left[WIDTH] + len(piece[0])
    # getting the final row/column allowed
    final_height = min(max_rows_allowed, expected_height)
    final_width = min(max_columns_allowed, expected_width)
    # piece counters
    piece_row = 0
    piece_column = 0
    for row in range(upper_left[HEIGHT], final_height):
        for column in range(upper_left[WIDTH], final_width):
            image[row][column] = piece[piece_row][piece_column]
            piece_column += 1
        # reset row, add column
        piece_column = 0
        piece_row += 1


def average(image):
    number_of_pixels = len(image) * len(image[0])  # pixels are rows * columns
    red_list = []
    green_list = []
    blue_list = []

    # extracting vales for each pixel
    for row in range(len(image)):
        for column in range(len(image[0])):
            red_list.append(image[row][column][RED])
            green_list.append(image[row][column][GREEN])
            blue_list.append(image[row][column][BLUE])

    # averaging
    average_red = sum(red_list) / number_of_pixels
    average_green = sum(green_list) / number_of_pixels
    average_blue = sum(blue_list) / number_of_pixels

    return average_red, average_green, average_blue


def preprocess_tiles(tiles):
    """
    A function that takes a list of tiles and returns the average colors
    in each one in a list, such as that that the i'th place in the list
    is the average colors of the i'th tile
    """
    average_color_list = []
    for tile in tiles:
        average_for_tile = average(tile)
        average_color_list.append(average_for_tile)
    return average_color_list


def get_best_tiles(objective, tiles, averages, num_candidates):
    # first we will get the average fo the objective
    objective_avg = average(objective)
    # getting list of distances to work with
    list_of_distances = []
    for tile_average in averages:
        list_of_distances.append(compare_pixel(objective_avg, tile_average))

    # finding the indices for candidates
    candidates_indices_list = []
    for i in range(num_candidates):
        for (k, distance) in enumerate(list_of_distances):
            if k in candidates_indices_list:
                continue
            elif distance == min(list_of_distances[k:]):
                candidates_indices_list.append(k)

    # making the candidate list
    candidate_list = []
    for index in candidates_indices_list:
        candidate_list.append(tiles[index])

    return candidate_list


def choose_tile(piece, tiles):
    list_of_comparisons = []
    for tile in tiles:
        tile_distance = compare(piece, tile)
        list_of_comparisons.append(tile_distance)
    min_distance = min(list_of_comparisons)
    min_index = list_of_comparisons.index(min_distance)
    return tiles[min_index]


def make_mosaic(image, tiles, num_candidates):
    # parameters, assuming all tiles are the same size
    image_height = len(image)
    image_width = len(image[0])
    print(image_height, image_width)
    tile_possessed_height = len(tiles[0])
    tile_possessed_width = len(tiles[0][0])
    print(tile_possessed_height, tile_possessed_width)
    print('prepreccesing tiles')
    tile_averages = preprocess_tiles(tiles)
    print('preprecces tiles DONE')
    # a tuple for each section's size
    section_size = (tile_possessed_height, tile_possessed_width)
    # counter indexes
    current_row = 0
    current_column = 0
    while current_row < image_height:  # a loop for each row
        while current_column < image_width:  # a loop for each column
            current_upper_left = (current_row, current_column)
            print(current_upper_left)
            original_piece = get_piece(image, current_upper_left, section_size)
            tile_candidates = get_best_tiles(original_piece, tiles,
                                             tile_averages, num_candidates)
            best_tile = choose_tile(original_piece, tile_candidates)
            set_piece(image, current_upper_left, best_tile)
            current_column += tile_possessed_width
            print('DONE')
        # reset column and add row
        current_column = 0
        current_row += tile_possessed_height

    return image



# if __name__ == '__main__':
#     if len(sys.argv) == NUMBER_OF_ARGUMENTS + 1:
#         image_source = sys.argv[1]
#         image_dir = sys.argv[2]
#         output_name = sys.argv[3]
#         tile_height_input = int(sys.argv[4])
#         num_candidates_input = int(sys.argv[5])
#         if tile_height_input <= 0:
#             print('tile height MUST be larger then 0')
#             quit()
#         if num_candidates_input <= 0:
#             print('number of candidates MUST be larger then 0')
#             quit()
#         source_image = mosaic.load_image(image_source)
#         print('procces tiles STARTED')
#         tiles_base = mosaic.build_tile_base(image_dir, tile_height_input)
#         print('procces tiles COMPLETE')
#         mosaic_image = make_mosaic(source_image, tiles_base, num_candidates_input)
#         mosaic.save(mosaic_image, output_name)
#         mosaic.show(mosaic_image)
#     else:
#         print(WRONG_ARG)

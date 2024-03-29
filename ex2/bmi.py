import math


def is_normal_bmi(weight, height):
    """Takes weight(in kg) and height(in meters) to tell the user
    weather he's on the standard weight for his height
     """
    bmi_value = weight / math.pow(height, 2)
    if bmi_value < 18.5 or bmi_value > 24.9:
        return False
    else:
        return True


print(is_normal_bmi(65,1.7))
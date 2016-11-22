##############################################
# FILE: hello_turtle.py
# WRITER: Or Mizrahi, Xelanos, 308484625
# DESCRIPTION: makes a flower bed
##############################################
import turtle

NORMAL_TURN = 90  # 90 degrees tuen
HALF_TURN = 45  # 45 degrees tuen
HARD_TURN = 135  # 135 degrees turn
U_TURN = 180  # 180 degrees turn
FORWARD = 30  # 30 steps
STEM_SIZE = 150  # flowe stem size
FLOWER_DISTANCE = 150  # distance between flowers
GO_TO_START = 200  # distance to start


def draw_petal():
    """ Make turtle draw a lonely petal """
    turtle.forward(FORWARD)
    turtle.left(HALF_TURN)
    turtle.forward(FORWARD)
    turtle.left(HARD_TURN)
    turtle.forward(FORWARD)
    turtle.left(HALF_TURN)
    turtle.forward(FORWARD)
    turtle.left(HARD_TURN)  # reset turtle heading


def draw_flower():
    """ Make turtle draw a pretty flower """
    turtle.right(HALF_TURN)  # correct heading
    draw_petal()  # first pretal
    turtle.right(NORMAL_TURN)
    draw_petal()  # second petal
    turtle.right(NORMAL_TURN)
    draw_petal()  # third petal
    turtle.right(NORMAL_TURN)
    draw_petal()  # last petal
    turtle.right(HARD_TURN)
    turtle.forward(STEM_SIZE)  # draw stem


def draw_flower_advanced():
    """ Make turtle draw a pretty flower and also moves him
    to prepare for another
    """
    draw_flower()
    turtle.left(NORMAL_TURN)  # correct heading
    turtle.up()  # deactivate drawing
    turtle.forward(FLOWER_DISTANCE)  # take distance betweem flowers
    turtle.left(NORMAL_TURN)
    turtle.forward(STEM_SIZE)  # Compensate stem size
    turtle.right(NORMAL_TURN)  # reset turtle heading
    turtle.down()  # activate drawing


def draw_flower_bed():
    """ Make turtle draw a lovely little flower bed """
    # Get turtle to start position
    turtle.up()  # deactivate drawing
    turtle.left(U_TURN)
    turtle.forward(GO_TO_START)
    turtle.right(U_TURN)
    turtle.down()  # activate drawing

    # draw the flower bed
    draw_flower_advanced()
    draw_flower_advanced()
    draw_flower_advanced()

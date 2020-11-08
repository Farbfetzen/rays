# Note about FOV and appearance of the walls:
# The aspect ratio of the walls depends on the fov, the aspect ratio of the
# window, and the value of h in this line: line_height_half = h / wall_distance.
# They look square when the fov is 66°, the aspect ratio is 4:3 and h is half
# the display height. Consider this when changing any one of those three values.


import math


DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 900
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
FPS = 60
DT_LIMIT = 2 / FPS  # half the time of one normal frame

MOVE_FORWARD = "move forward"
MOVE_BACKWARD = "move backward"
MOVE_LEFT = "move left"
MOVE_RIGHT = "move right"
ROTATE_LEFT = "rotate left"
ROTATE_RIGHT = "rotate right"
TOGGLE_DEV_OVERLAY = "toggle dev overlay"
PAUSE = "pause"

DEFAULT_OPTIONS = {
    "controls": {
        MOVE_FORWARD: "w",
        MOVE_LEFT: "a",
        MOVE_BACKWARD: "s",
        MOVE_RIGHT: "d",
        ROTATE_LEFT: "q",
        ROTATE_RIGHT: "e",
        PAUSE: "p",
        TOGGLE_DEV_OVERLAY: "f1"
    },
    "camera": {
        "fov_degrees": 66,
        "move_speed": 5,  # squares / s
        "rotate_speed_keyboard": math.pi,  # radians / s
        "rotate_speed_mouse": math.pi / DISPLAY_WIDTH,  # radians / pixel
        "rotate_speed_mouse_multiplier": 1.5
    }
}

BACKGROUND_COLOR = (32, 32, 32)

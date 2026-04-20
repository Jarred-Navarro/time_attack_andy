import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Physics Constants
GRAVITY = 0.5
PLAYER_JUMP_VELOCITY = 5.5
PLAYER_MOVE_ACCEL = 0.7
PLAYER_FRICTION = 0.6

# Velocity Constants
CRAWL_VELOCITY = 0.5
NORMAL_VELOCITY = 1.5
SPRINT_VELOCITY = 2.5

# Max jumps
MAX_JUMPS = 2
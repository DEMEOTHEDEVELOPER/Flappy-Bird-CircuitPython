#!/usr/bin/env python3
# Created By: Alex De Meo
# Date: 03/25/2022
# Description: This is my constants file for the edge badge

# EdgeBadge screen size is 160x128 and Sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
# Screen grid size
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
# Size of the characters
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
TOTAL_NUMBER_OF_LAZERS = 8
####SPEEDS####
SHIP_SPEED = 1
ALIEN_SPEED = 1
LAZER_SPEED = 2

#### BOUNDARIES ####
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE

# how many times the screen updates every second
FPS = 60
# How fast every sprite can move
SPRITE_MOVEMENT_SPEED = 1

# Button state is a dictionary that holds key value pairs
# first element is the key, second is the value

button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}

# This is a palette that tells the edgeBadge what colors it can use
RED_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)

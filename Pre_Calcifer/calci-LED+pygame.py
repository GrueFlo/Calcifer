# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

#Importing Neopixel
import time
import board
import neopixel


#_______________NEOPIXEL

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 30

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

#_______________PYGAME
# Importing the pygame module
import pygame
from pygame.locals import *

# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()

# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((600, 600))


# Create a list of different sprites
# that you want to use in the animation
image_sprite = [pygame.image.load("Sprite1.png"),
				pygame.image.load("Sprite2.png")]


# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()

# Creating a new variable
# We will use this variable to
# iterate over the sprite list
value = 0

# Creating a boolean variable that
# we will use to run the while loop
run = True



#_______________NEOPIXEL

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)



#____PYGAME

while run:

    # Setting the framerate to 3fps just
    # to see the result properly
    clock.tick(10)

    # Setting 0 in value variable if its
    # value is greater than the length
    # of our sprite list
    if value >= len(image_sprite):
        value = 0

    # Storing the sprite image in an
    # image variable
    image = image_sprite[value]

    # Creating a variable to store the starting
    # x and y coordinate
    x = 150

    # Changing the y coordinate
    # according the value stored
    # in our value variable
    if value == 0:
        y = 200
    else:
        y = 265

    # Displaying the image in our game window
    window.blit(image, (x, y))

    # Updating the display surface
    pygame.display.update()

    # Filling the window with black color
    window.fill((0, 0, 0))

    # Increasing the value of value variable by 1
    # after every iteration
    value += 1


    #____________Neopixel
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
    pixels.show()
    time.sleep(0.5)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
    pixels.show()
    time.sleep(0.5)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    pixels.show()
    time.sleep(0.5)

    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
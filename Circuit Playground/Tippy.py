from adafruit_circuitplayground import cp

import random
import time

while True:
    x, y, z = cp.acceleration
    if x > .5:
        cp.pixels[1](43,188,187)
        cp.pixels[2](43,188,187)
        cp.pixels[3](43,188,187)
        cp.pixels[6](0,0,0)
        cp.pixels[7](0,0,0)
        cp.pixels[8](0,0,0)
    if x < -.5:
        cp.pixels[1](0,0,0)
        cp.pixels[2](0,0,0)
        cp.pixels[3](0,0,0)
        cp.pixels[6](43,188,187)
        cp.pixels[7](43,188,187)
        cp.pixels[8](43,188,187)
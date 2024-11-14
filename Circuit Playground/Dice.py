# We first need to import board specific tools
# Every project for this board will need this statement
import time
import random

from adafruit_circuitplayground import cp


while True:
     if cp.button_a == True:
        random_number = random.randint(1, 11)
        if cp.button_a == True:
            if random_number == 1:
                cp.pixels[0](190,204,65)
            elif random_number == 2:
                cp.pixels[0](190,204,65)
                cp.pixels[1](190,204,65)
            elif random_number == 3:
                cp.pixels[0](190,204,65)
                cp.pixels[1](190,204,65)
                cp.pixels[2](190,204,65)
            elif random_number == 4:
                cp.pixels[0](190,204,65)
                cp.pixels[1](190,204,65)
                cp.pixels[2](190,204,65)
                cp.pixels[3](190,204,65)
            elif random_number == 5:
                cp.pixels[0](190,204,65)
                cp.pixels[1](190,204,65)
                cp.pixels[2](190,204,65)
                cp.pixels[3](190,204,65)
                cp.pixels[4](190,204,65)
            elif random_number == 6:
                cp.pixels[0](190,204,65)
                cp.pixels[1](190,204,65)
                cp.pixels[2](190,204,65)
                cp.pixels[3](190,204,65)
                cp.pixels[4](190,204,65)
                cp.pixels[5](190,204,65)
            elif random_number == 7:
                cp.pixels[0](190,204,65)
                cp.pixels[1](190,204,65)
                cp.pixels[2](190,204,65)
                cp.pixels[3](190,204,65)
                cp.pixels[4](190,204,65)
                cp.pixels[5](190,204,65)
                cp.pixels[6](190,204,65)
            elif random_number == 8:
                cp.pixels[0](190,204,65)
                cp.pixels[1](190,204,65)
                cp.pixels[2](190,204,65)
                cp.pixels[3](190,204,65)
                cp.pixels[4](190,204,65)
                cp.pixels[5](190,204,65)
                cp.pixels[6](190,204,65)
                cp.pixels[7](190,204,65)
            elif random_number == 9:
                cp.pixels[0](190,204,65)
                cp.pixels[1](190,204,65)
                cp.pixels[2](190,204,65)
                cp.pixels[3](190,204,65)
                cp.pixels[4](190,204,65)
                cp.pixels[5](190,204,65)
                cp.pixels[6](190,204,65)
                cp.pixels[7](190,204,65)
                cp.pixels[8](190,204,65)
            elif random_number == 10:
                cp.pixels[0](190,204,65)
                cp.pixels[1](190,204,65)
                cp.pixels[2](190,204,65)
                cp.pixels[3](190,204,65)
                cp.pixels[4](190,204,65)
                cp.pixels[5](190,204,65)
                cp.pixels[6](190,204,65)
                cp.pixels[7](190,204,65)
                cp.pixels[8](190,204,65)
                cp.pixels[9](190,204,65)

     if cp.button_b == True:
          cp.pixels.fill((0,0,0))